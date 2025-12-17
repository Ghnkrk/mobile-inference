import os
from huggingface_hub import snapshot_download

# -------------------------------------------------
# Config (edit this to change the model)
# -------------------------------------------------

MODEL_NAME = "Qwen/Qwen2.5-3B"   # change this to any HF model repo
SAVE_DIR = "./qwen_model"        # local folder to save the model


def main():
    os.makedirs(SAVE_DIR, exist_ok=True)

    print(f"📥 Downloading model: {MODEL_NAME}")
    print(f"📁 Saving to: {os.path.abspath(SAVE_DIR)}\n")

    snapshot_download(
        repo_id=MODEL_NAME,
        local_dir=SAVE_DIR,
        local_dir_use_symlinks=False
    )

    print("\n✅ Model download complete!")


if __name__ == "__main__":
    main()
