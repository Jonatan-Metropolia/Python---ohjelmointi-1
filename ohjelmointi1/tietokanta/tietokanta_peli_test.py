CREATE TABLE locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    coordinates POINT NOT NULL,

    -- optional: make sure coordinates are valid
    SPATIAL INDEX(coordinates)
);
INSERT INTO locations (name, coordinates)
VALUES ('Eiffel Tower', POINT(2.2945, 48.8584));
SELECT name, ST_Distance_Sphere(coordinates, POINT(-73.9857, 40.7484)) AS distance_meters
FROM locations
ORDER BY distance_meters ASC
LIMIT 5;
SELECT 
    id,
    name,
    ST_Distance_Sphere(coordinates, POINT(@lng, @lat)) AS distance_meters
FROM locations
WHERE ST_Distance_Sphere(coordinates, POINT(@lng, @lat)) <= @radius
ORDER BY distance_meters;

