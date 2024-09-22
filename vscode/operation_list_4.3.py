for value in range(1, 11):
    print(value)
    print(f"The value is {value} !")

list1=list(range(1,101))
print(list1)
list2=list(range(0,101,5))
print(list2)
squares = []
for i in range(1, 100+1):
    squares.append(i**2)
print(squares)
digits = [0,1,4,20,-19,2,3,5,6,7,8,9]
print(digits)
digits.sort()
print(digits)
print(digits[3])
print(min(digits))
print(max(digits))
print(sum(digits))
print(len(digits))
squares = [i**3 for i in range(0,27,3)]
print(squares)

list1 = [i**2 for i in range(1,100)]
print(list1)
print(sum(list1))



