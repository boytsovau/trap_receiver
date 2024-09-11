import os
import json


def get_path(folder) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, folder)


def open_file(folder, file=None) -> dict:
    path = f'{get_path(folder)}/{file}'
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {path} not found.")
        return {}
