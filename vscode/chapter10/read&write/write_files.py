from pathlib import Path

path = Path('vscode/chapter10/porgramming.txt')#如果文件不存在，则创建文件
#path.write_text('I love programming.')#向文件中写入内容
contents = "I love programming.\n"
contents += "I also love creating new things.\n"
contents += "I also love working with other people.\n"
path.write_text(contents)



