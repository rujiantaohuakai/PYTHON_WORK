from random import random, choice

numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E')
lottery_numbers = [choice(numbers) for i in range(1, 8)]
lottery_number = ''
for number in lottery_numbers:
    lottery_number += number
print(f"If your lottery number is {lottery_number}, you can get 1000000000000$")

my_ticket = []
times = 0
while my_ticket != lottery_numbers:
    my_ticket = [choice(numbers) for i in range(1, 8)]
    times += 1

print(my_ticket)
print(lottery_numbers)
print(times)


