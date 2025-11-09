import subprocess
from pathlib import Path

def run_chandra(input_path: str, output_dir: str, method: str = "vllm"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    if method == "hf":
        cmd = ["python", "-m", "chandra_hf", input_path, output_dir]
    else:
        cmd = ["python", "-m", "chandra_vllm", input_path, output_dir]

    try:
        subprocess.run(cmd, check=True)
        print(f"OCR valmis! Tulokset löytyvät kansiosta: {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"OCR epäonnistui: {e}")

input_path = r"C:\Users\Käyttäjä\Koulu\img_to_text\input\testikuva.png"
output_dir = r"C:\Users\Käyttäjä\Koulu\img_to_text\output"

if __name__ == "__main__":
    run_chandra(input_path, output_dir)

#& "C:\Users\Käyttäjä\AppData\Roaming\Python\Python313\Scripts\chandra.exe" "C:\Users\Käyttäjä\Koulu\img_to_text\input\testikuva.png" "C:\Users\Käyttäjä\Koulu\img_to_text\output"
