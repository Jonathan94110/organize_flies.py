# organize_flies.py
A Python script that organizes files on your desktop into categorized folders based on file types, such as Images, Documents, Videos, Audio, Archives, and Others. (MAC OS)
# Desktop File Organizer

**Desktop File Organizer** is a Python script that automatically organizes files on your desktop into categorized folders based on their file extensions. It helps keep your workspace clean and easy to navigate.

## Features
- Categorizes files into folders (e.g., Images, Documents, Videos, Audio, Archives).
- Creates a "Others" folder for uncategorized files.
- Fully customizable file categories.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/desktop-file-organizer.git
   cd desktop-file-organizer


   	2.	Set Up Python Environment (Optional but recommended):

python3 -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows

python3 organize_files.py


How It Works

	1.	The script scans your desktop for files.
	2.	It categorizes them into folders like Images, Documents, etc., based on their extensions.
	3.	If no matching category is found, the file is placed in an “Others” folder.

Customization

You can edit the file_categories dictionary in the script to add or modify file types and categories.

Example Folder Organization

	•	Images: .jpg, .png, .gif, etc.
	•	Documents: .pdf, .docx, .txt, etc.
	•	Videos: .mp4, .mov, .avi, etc.
	•	Audio: .mp3, .wav, .flac, etc.
	•	Archives: .zip, .rar, .tar, etc.
	•	Others: Any uncategorized file types.

Contributing

Feel free to fork this repository and submit pull requests. Feedback and contributions are always welcome!
