import pyperclip
# 6.4 ord() and chr() ASCII和字符的转化
Letters = []
letter = 'A'
print(ord(letter))
print(chr(ord(letter)+1))
for i in range(26):
    Letters.append(chr(ord(letter)+i))
print(Letters)

for letter in Letters:
    print(f"{letter}'s unicode is {ord(letter)}")
#6.5 pyperclip模块复制粘贴字符
print(pyperclip.paste())    # 将粘贴板里的内容打印出来
pyperclip.copy('Hello,  world!!!')   # 将字符串复制到粘贴板
print(pyperclip.paste())







