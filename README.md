# Google-Photos-Cleaner
A simple Python script to clean up Google Takeout photos by:  
- Deleting `.json` files exported by Google Takeout
- Renaming Google Motion Photo `.MP` files to `.mp4` 

The script recursively scans a folder and its subfolders.



## Requirements

- Python
- Tested on Windows



## Usage

1. run this command
```bash
python clean_motion_photos.py
```
2. Enter the full path to your Google Photos folder when prompted.



## Notes 
- The script does not backup files, so make sure your original Takeout folder is safely stored before running.
- After running, all .json files will be deleted and all .MP files will be renamed to .mp4.
- Inspired by [hedgetech77/clean-google-takeout-json](https://github.com/hedgetech77/clean-google-takeout-json).
