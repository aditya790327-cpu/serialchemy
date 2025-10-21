import os
import shutil
from datetime import datetime

# === CONFIGURATION ===
# Directory to organize
TARGET_DIR = r"C:\Users\YourName\Downloads"  # Change this to your folder path

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programs": [".exe", ".msi", ".bat", ".sh", ".py"],
    "Others": []
}

def organize_files(directory):
    print(f"📂 Starting organization for: {directory}\n")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Determine category
        category = None
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                category = folder
                break
        if not category:
            category = "Others"

        # Create target folder
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

        # Move the file
        dest_path = os.path.join(folder_path, filename)
        try:
            shutil.move(file_path, dest_path)
            print(f"✅ Moved: {filename} → {category}")
        except Exception as e:
            print(f"⚠️ Could not move {filename}: {e}")

    print("\n🎉 Organization complete!")
    print(f"🕒 Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    organize_files(TARGET_DIR)
