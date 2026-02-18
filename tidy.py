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

def organize(folder=None, dry_run=False):
    if folder is None:
        if len(sys.argv) < 2:
            print("Usage: tidy <folder_path> [--dry-run]")
            return
        folder = sys.argv[1]

    if not os.path.isdir(folder):
        print("Invalid folder path")
        return

    print("Preview mode ON" if dry_run else "Organizing files...")

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isdir(path):
            continue

        _, ext = os.path.splitext(file)
        category = get_category(ext)

        target_dir = os.path.join(folder, category)
        os.makedirs(target_dir, exist_ok=True)

        destination = os.path.join(target_dir, file)

        if dry_run:
            print(f"[DRY RUN] {file} -> {category}")
        else:
            try:
                shutil.move(path, destination)
                print(f"Moved: {file} -> {category}")
            except Exception as e:
                print(f"Skipped: {file} ({e})")

    print("Done")

if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    organize(dry_run=dry)
