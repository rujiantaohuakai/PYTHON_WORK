from pathlib import Path
import json

path = Path("username.json")
contents = path.read_text()
username = json.loads(contents)  # json.loads()将一个json格式的字符串作为参数，并返回一个python对象。
print(f"Welcome back, {contents}!")
print(f"Welcome back, {username}!")

