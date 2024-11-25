import os
import shutil

# Path to your desktop (customize if needed)
desktop_path = os.path.expanduser("~/Desktop")

# File type categories and their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Others": []  # Catch-all for uncategorized files
}

# Function to organize files
def organize_files(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file category
        file_extension = os.path.splitext(file_name)[1].lower()
        moved = False

        for category, extensions in file_categories.items():
            if file_extension in extensions:
                category_path = os.path.join(directory, category)
                os.makedirs(category_path, exist_ok=True)
                shutil.move(file_path, os.path.join(category_path, file_name))
                moved = True
                break

        # If no matching category, move to "Others"
        if not moved:
            others_path = os.path.join(directory, "Others")
            os.makedirs(others_path, exist_ok=True)
            shutil.move(file_path, os.path.join(others_path, file_name))

# Run the script
if __name__ == "__main__":
    organize_files(desktop_path)
    print("Files organized successfully!")