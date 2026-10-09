


a = [1, 'Ajay', 2, 3,6,8, 5, 'seema', 'anita']

numbers = []

for i in a:
    if type(i) == int:
        numbers.append(i)

maximum = max(numbers)

index = a.index(maximum)

list1 = a[:index]
list2 = a[index:]

print(list1)
print(list2)