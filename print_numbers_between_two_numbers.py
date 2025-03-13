#print all numbers between the two numbers

num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter a number: '))

number_between = []
if num_1 < num_2:
    for i in range(num_1 + 1, num_2):
            number_between.append(i)
elif num_1 > num_2:
    for i in range(num_1 - 1, num_2, -1):       # reversed the order
            number_between.append(i)
elif num_1 == num_2:
        print('The numbers are equal.')

print(number_between)