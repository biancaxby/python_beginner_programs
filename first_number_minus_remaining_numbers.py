#first number minus the remaining numbers

#ask user for a number
num_1 = int(input('Enter a number: '))

#for loop will ask user to add more numbers
for i in range(9):
    numbers = int(input('Enter a number: '))

sums =  i + numbers
  
difference =  sums - num_1

print(difference)