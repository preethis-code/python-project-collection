import os
import shutil

# Folder path (change this to your folder)
path = "C:/Users/1260p/Desktop/py proj/File Organizer/test_folder"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

# Get all files in the folder
files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)

    # Skip if it's already a folder
    if os.path.isdir(file_path):
        continue

    # Get file extension
    ext = os.path.splitext(file)[1].lower()

    moved = False

    for folder, extensions in file_types.items():
        if ext in extensions:
            folder_path = os.path.join(path, folder)

            # Create folder if not exists
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            shutil.move(file_path, os.path.join(folder_path, file))
            moved = True
            break

    # If file type not found → move to "Others"
    if not moved:
        other_path = os.path.join(path, "Others")

        if not os.path.exists(other_path):
            os.makedirs(other_path)

        shutil.move(file_path, os.path.join(other_path, file))

print("Files organized successfully!")