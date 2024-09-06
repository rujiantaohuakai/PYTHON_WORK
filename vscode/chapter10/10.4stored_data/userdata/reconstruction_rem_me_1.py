from pathlib import Path
import json


def get_stored_username(path):
    """如果存储了用户名称，则获取它"""
    if path.exists():
        contents = path.read_text()  # 读入再转换
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """如果没有用户名，则输入"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """问候用户，指出其姓名"""
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"We will remember you when you come back, {username}!")


greet_user()


