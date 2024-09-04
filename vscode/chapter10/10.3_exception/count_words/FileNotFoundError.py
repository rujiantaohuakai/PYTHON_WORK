from pathlib import Path


def count_words(path):
    """计算一个文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exit.")
        pass #静默，不显示捕获到异常
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
        num_the = contents.count('the ')
        # num_the = contents.count('the') 结果不同，会计算they，them，等等单词中的the
        print(f"The word 'the ' appears {num_the} times in the text")


path1 = Path('alice.txt')
count_words(path1)
print('\n')

"""
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
    #print(words)
"""

filenames = ['alice.txt', 'Siddhartha.txt', 'Muir.txt', 'Moby Dick.txt', 'Little Women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

