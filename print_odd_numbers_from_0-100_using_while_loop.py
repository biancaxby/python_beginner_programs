#print all odd numbers form 0-100 using while loop

#while loop will repeat 100 times and then divide the numbers to two
number = 0
while number < 100:
    number += 1
    if number % 2 != 0:
        print(number)
