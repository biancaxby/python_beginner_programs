#print all numbers between the two numbers



num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter a number: '))

while True:
    if num_1 < num_2:
        for i in range(num_1 - num_2):
            num_1 += 1 
            if num_1 >= num_2:
                break
    if num_1 > num_2:
        num_1 -= num_2
        if num_1 <= num_2:
            break

print(num_1)
