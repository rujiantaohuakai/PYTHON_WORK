def greet_user(name):
    """显示简单的问候语"""
    print(f"{name.title()}, Hello World!")


"""
name1 = input("What is your name? Please tell me: ")
greet_user(name1)
"""


def describe_pet(pet_name, animal_type='dog'):
    """描述宠物"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


"""
pet_name1 = input("What is your pet's name?")
describe_pet(pet_name1)
describe_pet('Muir', 'human')
"""


def get_formatted_name(first_name='', last_name=''):
    """返回一个人完整的名字"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


"""
full_name1 = get_formatted_name('li', 'muir')
print(full_name1)
"""


def build_person(first_name, last_name, age=None, company=None, middle_name=None):
    person = {'first_name': first_name.title(), 'last_name': last_name.title()}
    if age:
        person['age'] = age
    if company:
        person['company'] = company.title()
    if middle_name:
        person['middle_name'] = middle_name.title()
    return person


"""
person1 = build_person('li', 'peiyang', company='Henu', age=18)
print(person1)
person1['age'] += person1['age']
print(person1)
"""


"""
while True:
    print("enter 'q' at any time to quit")
    first = input("your first_name: ")
    if first == 'q':
        break
    last = input("your last_name: ")
    if last == 'q':
        break
    full_name2 = get_formatted_name(first,last)
    print(f"Hello, {full_name2}\n")
"""
########################################################################################################################


def greet_users(names):
    """向列表中的每个用户发出简单的问候"""
    for name in names:
        print(f"Hello, {name}, have a nice day!")


usernames = ['alice', 'bob', 'muir', 'taohua']
greet_users(usernames)
########################################################################################################################


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计
    打印每个设计后，都将其转移到列表：completed_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Print model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['design_a', 'design_b', 'design_c', 'design_b']
completed_models = []
print_models(unprinted_designs[:], completed_models) #使用切片来保留原始列表
show_completed_models(completed_models)
print(unprinted_designs)
print("\n")
########################################################################################################################


def show_messages(messages, sent_messages=[]):
    """展示列表里的信息"""
    if messages:
        for message in messages:
            print(message)
    else:
        print(messages)

    for sent_message in sent_messages:
        print(sent_message)


def send_messages(messages, sent_messages):
    """将messages列表里的信息打印并且转移到sent_messages中"""
    messages.reverse() #保持信息原本的顺序
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


messages = ['hello', 'how are you', 'i love you', 'you are my best friend']
sent_messages = []
show_messages(messages)
print("\n")
send_messages(messages, sent_messages)
print("\n")
show_messages(messages, sent_messages)
########################################################################################################################


def make_pizza(size, *toppings):
    """显示要制作披萨的大小，并且接受多个实参作为配料表"""
    print(f"\nyou pizza size is {size}, and it was made with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(100, 'pepperoni', 'mushrooms', 'green peppers', 'extra cheese', 'mushrooms')
make_pizza(18, 'beef')
########################################################################################################################


def user_profile(first, last, **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


user1 = user_profile('li', 'peiyang', school='Henu', hometown='handan')
print(user1)
########################################################################################################################


def make_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs


car1 = make_car('subaru', 'outback', color='black', tow_package=True)
if car1['tow_package']:
    print(car1)


########################################################################################################################













