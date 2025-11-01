import os
import gdown

def download_large_files():
    files = {
        "model/tag_sim.npy": "https://drive.google.com/uc?export=download&id=YOUR_TAG_SIM_FILE_ID",
        "model/movie_tag_matrix.pkl": "https://drive.google.com/uc?export=download&id=1l99nPAKwbEhiCZLSncsK7i9d8x_3tfyT",
    }

    for file_path, url in files.items():
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            print(f"Downloading {file_path} from Google Drive...")
            gdown.download(url, file_path, quiet=False)
        else:
            print(f"{file_path} already exists, skipping download.")
