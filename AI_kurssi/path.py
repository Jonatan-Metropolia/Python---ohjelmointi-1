import subprocess

input_path = r"C:\Users\Käyttäjä\Koulu\img_to_text\input\testikuva.png"
output_dir = r"C:\Users\Käyttäjä\Koulu\img_to_text\output"

# Käytetään samaa Pythonia kuin PyCharm
subprocess.run(["python", "-m", "chandra", input_path, output_dir], check=True)

print("OCR valmis! Tarkista output-kansio.")
