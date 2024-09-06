from pathlib import Path
import json

numbers =[2, 3, 5, 7, 11, 13]

# json.dumps() 将数据保存到xxx.json文件中，保存内容与python输出相同
path = Path('number.json')
contents = json.dumps(numbers)
path.write_text(contents)

# json.loads() 将数据读取到内存中
path1 = Path('number.json')
contents = path.read_text()
new_numbers = json.loads(contents) # 返回一个对象，这里为返回一个列表
for number in new_numbers:
    print(number)
print(new_numbers)


