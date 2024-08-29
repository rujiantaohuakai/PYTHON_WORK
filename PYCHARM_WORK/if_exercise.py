# 5.3
alien1_color = "green"
alien2_color = "red"
if alien1_color == "green":
    print("Get five points!")
if alien2_color == "green":
    print("Get five points!")
else:
    print("No points.")
# 5.5
alien3_color = "red"
if alien3_color == "green":
    print("Get five points!")
elif alien3_color == "yellow":
    print("Get ten points!")
else:
    print("Get fifteen points!")
# 5.7
favorite_fruits = ("apple", "banana", "peach", "pear", "strawberry")
if "pear" in favorite_fruits:
    print("I know you like pear!")
for fruit in favorite_fruits:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}")
        print("You really like " + fruit)
fruit1 = "orange"
if fruit1 not in favorite_fruits:
    print(f"you do not like {fruit1}!")
# 5.8
users = ["taohua", "Jaden", "Muir", "peiyang", "gefei"]
for user in users:
    if user == "Muir":
        print("Hello Muir, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again!")
# 5.9
users1 = {}
if not users1:
    print("We need to find some users！")
else:
    for user1 in users1:
        if user1 == "Muir":
            print("Hello Muir, would you like to see a status report?")
        else:
            print(f"Hello {user1}, thank you for logging in again!")
# 5.10
current_users = ["taohua", "Jaden", "Muir", "peiyang", "gefei"]
new_users = ["TaoHua", "bob", "MUIR", "lang"]
lower_current_users = []

for user in current_users:
    lower_current_users.append(user.lower())
# 上两句可以替换为 lower_current_users = [user.lower() for user in current_users]

print(lower_current_users)
for user in new_users:
    if user.lower() in lower_current_users:
        print(f"{user} already exists！")
    else:
        print(f"{user} available！")
        current_users.append(user)
print(current_users)
# 5.11
number_list = [i for i in range(1, 10)]
print(number_list)
for number in number_list:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{str(number)}th")
