import os
from pathlib import Path

print("Current working directory:", os.getcwd())
#path = Path("c:/Users/li177/Desktop/python_work/vscode/chapter10/pi_digits.txt")
path = Path("vscode/chapter10/pi_digits.txt")
try:
    contents = path.read_text()
    print(f"{contents} is the contents of {path}.(before removing spaces in the last line)")
    print(f"{contents.rstrip()} is the contents of {path}.(after removing spaces in the last line)")
except FileNotFoundError:
    print(f"The file {path} does not exist.")
