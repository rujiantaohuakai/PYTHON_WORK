bicycles = ['trek', 'cannondale','redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
print(bicycles[-4])

motorcycles = ['honda', 'yamaha', 'ducati']
print(motorcycles)
print(motorcycles[0])
motorcycles[0]= 'ducati'
print(motorcycles)
print(motorcycles[0])

motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'test')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

pop=motorcycles.pop()
print(pop)
print(motorcycles)

motorcycles.append('test2')
motorcycles.insert(0, 'test1')
print(motorcycles)

first_owned = motorcycles.pop(0)
print(first_owned)
print(motorcycles)

cars=['bmw', 'audi', 'toyota', 'tesla']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars1 = ['bmw', 'audi', 'toyota', 'tesla']
cars2 = ['mercedes', 'ferrari', 'lamborghini', 'jaguar']
all_cars = cars1 + cars2
print(all_cars)

print("Here is the original list:")
print(cars1)
print("\nHere is the sorted list:")
print(sorted(cars1))
print("\nHere is the original list again:")
print(cars1)
print("\nHere is the sorted list in reverse order:")
print(sorted(cars1, reverse=True))
print("\nHere is the original list again:")
print(cars1)

print(cars2)
cars2.reverse()
print(cars2)
cars2.reverse()
print(cars2)
length=len(cars1)
print(length)
"""test"""
