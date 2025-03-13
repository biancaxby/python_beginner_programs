#print all numbers between the two numbers



num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter a number: '))

number_between = []
if num_1 < num_2:
    for i in range(num_1 + 1, num_2):
            number_between.append(num_1)
elif num_1 > num_2:
    for i in range(num_1 - 1, num_2, -1):       # reversed the order
            number_between.append(num_1)
    else:
        print('The numbers are equal.')

print(number_between)
            

