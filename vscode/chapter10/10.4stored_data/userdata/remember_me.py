from pathlib import Path
import json

path = Path('username.json')
if path.exists():  # 如果username.json存在，返回True、不存在返回false
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We will remember you when you come back, {username}!")
