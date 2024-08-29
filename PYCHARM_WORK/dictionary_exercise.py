# 6.1
person = {'first_name': 'li',
          'last_name': 'peiyang',
          'age': '19',
          'city': 'handan',
          }
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())
print(person)

for key,value in person.items():
    print(f"\nKey: {key}")
    print(f"Value: {value.title()}")

person['x_position'] = 0
person['y_position'] = 0
print(person)
person['x_position'] = 10
person['y_position'] = 20
print(person)
person['x_position'] = person['x_position'] + 100
print(person)
person['test1'] = 'hello'
print(person)
del person['test1']
print(f'\n{person}')
point_value = person.get('city', 'No point value assigned')
print(point_value.title())
print(person.get('test1', 'NO value assigned'))

for k,v in person.items():
    print(f'\nkey: {k}, value: {v}')
for k in person.keys():
    print(k.title())
print(person.keys())
keys = person.keys()
print(keys)
keys = sorted(person.keys())
print(keys)
print(sorted(person.keys()))
print('\n')
print(person.values())
for v in person.values():
    print(v)
person['test1'] = 'test'
person['test2'] = 'test'
print(person.values())
for v in set(person.values()):
    print(v)
set1 = {'a', 'b', 'c', 'd'}
for value in sorted(set1):
    print(value)
for value in set1:
    print(value)
favourite_language = {'a': 'C', 'b': 'c++', 'c': 'python', 'd': 'java'}
name_list = ('a', 'A', 'b', 'c', 'D', 'd', 'F')
for name in sorted(name_list):
    if name in favourite_language.keys():
        print(f'Thanks, {name}, I know your favourite is {favourite_language[name]}')
    else:
        print(f'Hi {name}, can you tell me your favourite language?')

for i in range(0,30):
    print(i)

aliens = []
for alien_number in range(0,31):
    new_alien = {'number': alien_number, 'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
points = 0;
for alien in aliens[5:11]:
    points += alien['points']
    print(alien)
print(points)
















