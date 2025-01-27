import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

PROJECT_NAME= "text_Summarizer"

files = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/conponents/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]



for file in files:
    file_path = Path(file)           #to avoid glitches in paths in different operator systems 
    dir_path, file_name = os.path.split(file_path)

    if dir_path != "":
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Created directory: {dir_path} for file : {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) ==0) :
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created file: {file_path}")

    else:
        logging.info(f"File: {file_path} already exists.")