"""
bulletPointAdder.py
This program adds bullet points to a given text file.
"""
import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')  # Split text into lines 以换行符分割文本
print(lines)
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)

print(pyperclip.paste())
