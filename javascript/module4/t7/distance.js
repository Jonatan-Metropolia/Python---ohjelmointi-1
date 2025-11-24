'use strict';

// Kartta
const map = L.map('map').setView([60.1785553, 24.8786212], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OSM</a> contributors',
}).addTo(map);

// Määränpään osoite
const destinationAddress = "Karaportti 2, Espoo";

// Geokoodaus funktio
async function geocode(address) {
    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(address)}`;
    const res = await fetch(url);
    const data = await res.json();
    if (data.length === 0) throw new Error("Osoitetta ei löytynyt: " + address);
    return { latitude: parseFloat(data[0].lat), longitude: parseFloat(data[0].lon) };
}

// Reitin hakeminen Digitransit
async function route(start, end) {
    const route_query = `{
        plan(
            from: {lat: ${start.latitude}, lon: ${start.longitude}}
            to: {lat: ${end.latitude}, lon: ${end.longitude}}
            numItineraries: 1
        ) {
            itineraries {
                legs {
                    startTime
                    endTime
                    mode
                    duration
                    distance
                    legGeometry { points }
                }
            }
        }
    }`;

    const api = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql';
    const fetch_options = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: route_query }),
    };

    const response = await fetch(api, fetch_options);
    const result = await response.json();

    const legs = result.data.plan.itineraries[0].legs;

    // Tyhjennetään vanhat reitit
    map.eachLayer(layer => {
        if (layer instanceof L.Polyline) map.removeLayer(layer);
    });

    // Piirretään legs
    for (let i = 0; i < legs.length; i++) {
        let color = '';
        const mode = legs[i].mode;

        if (mode === 'WALK') color = 'green';
        else if (mode === 'BUS') color = 'red';
        else if (mode === 'RAIL') color = 'cyan';
        else if (mode === 'TRAM') color = 'magenta';
        else if (mode === 'SUBWAY') color = 'orange';
        else color = 'blue';

        const points_obj = L.Polyline.fromEncoded(legs[i].legGeometry.points).getLatLngs();
        L.polyline(points_obj, { color }).addTo(map);
    }

    // Lisätään markerit
    L.marker([start.latitude, start.longitude]).addTo(map).bindPopup("Lähtö");
    L.marker([end.latitude, end.longitude]).addTo(map).bindPopup("Määränpää: Karaportti 2");

    map.fitBounds([
        [start.latitude, start.longitude],
        [end.latitude, end.longitude]
    ]);
}

// napin paino
document.getElementById('routeButton').addEventListener('click', async () => {
    const startAddr = document.getElementById('startAddress').value;
    try {
        const startCoords = await geocode(startAddr);
        const endCoords = await geocode(destinationAddress);
        route(startCoords, endCoords);
    } catch (err) {
        alert(err.message);
    }
});
