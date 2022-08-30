import os
from pathlib import Path

DIRS = {
    "Docs": [".doc", ".docx", ".pdf", ".xls", ".xlsx", ".pptx", ".csv", ".txt", ".od"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".png", ".psd"],
    "Software": [".deb", ".exe",".msi"],
    "Archives": [".zip", ".7z", ".gzip", ".tar"],
    "Os": [".iso", ".img"],
    "Js": [".js",".jsx"],
    "Css": [".css"]
    "Html": [".html"]
}


def findLocation(ext):
    for cat, extensions in DIRS.items():
        for extension in extensions:
            if extension == ext:
                return cat
    return "Others"


def organize():
    for item in os.scandir():
        if item.is_dir():
            continue
        file_path = Path(item)
        ext = file_path.suffix.lower()
        if ext == ".py":
            continue
        dir = findLocation(ext)
        dir_path = Path(dir)
        if dir_path.is_dir() != True:
            dir_path.mkdir()
        file_path.rename(dir_path.joinpath(file_path))


organize()
