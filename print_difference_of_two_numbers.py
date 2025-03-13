#2 nums print difference 

#ask user to input two numbers
num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter a number: '))

#swap values if the second number is bigger so that the answer is not in negative
if num_1 <num_2:
    num_1, num_2 = num_2, num_1

#print the difference of two numbers
diff = num_1 - num_2
print(diff)




