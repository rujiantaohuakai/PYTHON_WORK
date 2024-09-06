from random import randint
#radint(a,b) returns a random integer between a and b (inclusive)
#返回a到b之间的随机整数，包括a和b

class Die:
    """模拟一个骰子，可自定义骰子的面数"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die_size(self):
        print(randint(1,self.sides))

    @staticmethod
    def roll_die():
        print(randint(1, 6))


die1 = Die()
for i in range(1, 11):
    die1.roll_die_size()
print('\n')
# print('\n')
# for i in range(1, 11):
#     Die().roll_die()

die2 = Die(10)
die3 = Die(20)

for i in range(1, 11):
    die2.roll_die_size()
print('\n')
for i in range(1, 11):
    die3.roll_die_size()





















