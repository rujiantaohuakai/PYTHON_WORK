import os
from pathlib import Path

print("Current working directory:", os.getcwd())#打印当前工作目录
#path = Path("c:/Users/li177/Desktop/python_work/vscode/chapter10/pi_digits.txt")
path = Path("vscode/chapter10/pi_digits.txt")
try:
    contents = path.read_text()
    print(f"{contents} is the contents of {path}.(before removing spaces in the last line)")
    print(f"{contents.rstrip()} is the contents of {path}.(after removing spaces in the last line)")
except FileNotFoundError:
    print(f"The file {path} does not exist.")

try:
    contens1 = path.read_text().rstrip()#方法链式调用 rstrip方法去除字符串右侧的空格
    lines = contens1.splitlines()
    print(f"The file {path} has {len(lines)} lines.")
    print(lines)
    for line in lines:
        print(line)
except FileNotFoundError:
    print(f"The file {path} does not exist.")

pi_string = ""
for line in lines:
    pi_string += line.lstrip()#lstrip()方法去除字符串左侧的空格    strip()方法去除字符串两端的空格
print(f"The value of pi is {pi_string}.")
print(f"The length of pi_string is {len(pi_string)}")

#生日是否出现在pi_string中
birthday = input("Enter your birthday, in the form mmdd:")
if birthday in pi_string:
    print("Your birthday appears in the value of pi.")
else:
    print("Your birthday does not appear in the value of pi.")


