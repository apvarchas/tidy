import os
import shutil
import sys

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".flac"]
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize(folder=None):
    if folder is None:
        import sys
        if len(sys.argv) < 2:
            print("Usage: tidy <folder_path>")
            return
        folder = sys.argv[1]
    if not os.path.isdir(folder):
        print("Invalid folder path")
        return

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isdir(path):
            continue

        _, ext = os.path.splitext(file)
        category = get_category(ext)

        target_dir = os.path.join(folder, category)
        os.makedirs(target_dir, exist_ok=True)

        shutil.move(path, os.path.join(target_dir, file))

    print("Organization complete")

if __name__ == "__main__":
    organize()
