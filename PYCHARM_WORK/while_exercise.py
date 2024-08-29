'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

car = input("What kind of car would you like to rent? Please tell me: ")
print(f"Let me see if I can find you a {car}.")

number = input("Please tell me how many people will eat? number: ")
number = int(number)
if number > 8:
    print("Sorry, there is no extra tables")
elif 0 < number <= 8:
    print("OK, we have extra tables for you!")
else:
    print("Invalid number of people!")

number = input("Enter an integer and I will determine if it is an integer multiple of ten: ")
number = int(number)
if number % 10 == 0:
    print(f"Yes, {number} is an integer multiple of ten!")
else:
    print(f"No, {number} is not an integer multiple of ten")

current_number = 1
while current_number <= 100000:
    print(current_number)
    current_number += current_number
print(current_number)

current_number = 0
while current_number < 100:
    current_number += 1 #要放在前面，不能放到循环后面。因为会被continue跳过从而陷入死循环
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)
    # current_number += 2

current_number = 100
while current_number < 1000:
    current_number += 1
    list1 = []
    temp = current_number
    while temp != 0:
        list1.append(temp%10)
        temp //= 10
    list1_sum = 0
    for num in list1:
        list1_sum += num*num*num
    if list1_sum == current_number:
        print(current_number)


'''

import fun


messages = ['hello', 'how are you', 'i love you', 'you are my best friend']
sent_messages = []
fun.show_messages(messages)
print("\n")
fun.send_messages(messages, sent_messages)
print("\n")
fun.show_messages(messages, sent_messages)




