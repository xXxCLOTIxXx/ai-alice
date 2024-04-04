from datetime import datetime
from .config import (
    save_path
)

import os

class logger:
    session_date = datetime.now()

    def log(self, message: str, type: str = "INFO", save: bool = True, output: bool = True):
        print(f"[{datetime.now()}][{type}]: {message}")
        self.save(f"[{datetime.now()}][{type}]: {message}")
    
    def warn(self, message: str, output: bool = True, save: bool = True):
        self.log(type="WARNING", message=message, output=output, save=save)

    
    def save(self, message: str):
        try:os.makedirs(save_path)
        except FileExistsError: pass
        file = f"{save_path}/LOG-{self.session_date}.txt"
        with open(file, 'a') as f:
            f.write("\n"+message)