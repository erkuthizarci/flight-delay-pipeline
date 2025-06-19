import os
import subprocess

def download_dataset():
    kaggle_dataset = "usdot/flight-delays"
    output_path = "../data"

    print("Starting dataset download from Kaggle...")
    os.makedirs(output_path, exist_ok=True)

    cmd = [
        "kaggle", "datasets", "download",
        "-d", kaggle_dataset,
        "-p", output_path,
        "--unzip"
    ]

    try:
        subprocess.run(cmd, check=True)
        print("✅ Download complete.")
    except subprocess.CalledProcessError as e:
        print("❌ Download failed:", e)

if __name__ == "__main__":
    download_dataset()
