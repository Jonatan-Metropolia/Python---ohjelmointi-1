from PIL import Image

# Kuvien polut (muista tuplata kenoviivat \\ tai käytä r-stringiä)
paths = [
    r"C:\Users\Käyttäjä\Desktop\Koulu\matikka\WhatsApp Image 2025-08-29 at 21.24.49 (4).jpeg",
    r"C:\Users\Käyttäjä\Desktop\Koulu\matikka\WhatsApp Image 2025-08-29 at 21.24.49 (3).jpeg",
    r"C:\Users\Käyttäjä\Desktop\Koulu\matikka\WhatsApp Image 2025-08-29 at 21.24.49 (2).jpeg",
    r"C:\Users\Käyttäjä\Desktop\Koulu\matikka\WhatsApp Image 2025-08-29 at 21.24.49 (1).jpeg",
    r"C:\Users\Käyttäjä\Desktop\Koulu\matikka\WhatsApp Image 2025-08-29 at 21.24.49.jpeg"
]

# Avaa kuvat ja muunna RGB-muotoon (jos esim. jpg)
images = [Image.open(p).convert("RGB") for p in paths]

# Ensimmäisestä tehdään "pääkuva", loput lisätään perään
pdf_path = r"C:\Users\Käyttäjä\Desktop\Koulu\matikka\kaikki_kuvat.pdf"
images[0].save(pdf_path, save_all=True, append_images=images[1:])

print("PDF tallennettu:", pdf_path)
