from pathlib import Path

path = Path("vscode/chapter10/visitors.txt")
class Visitor:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def greet_visitor(self):
        return(f"Hello, {self.name}! Welcome to our website.")


visitor1 = Visitor()
visitor1.name = input("Please input your name:")
visitor1.age = input("Please input your age:")
path.write_text(f"Information of visitor: {visitor1.name}, {visitor1.age}. {visitor1.greet_visitor()}")
