#print how many odd numbers

#initialize odd counter
odd_counter = 0

#if print number if dividing it to two will not result to zero
for i in range(10):
    number = int(input('Enter a number: '))
    if number % 2 != 0:
        odd_counter += 1

print(odd_counter)
