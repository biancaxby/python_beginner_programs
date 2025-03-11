#how many even numbers 

#initialize the value of the counter
even_count = 0

#even_count will increase every time an odd number is inputed
for i in range(10):
    i = int(input('Enter a number: '))
    if i % 2 != 0:
        even_count += 1 

print(f' You have entered {even_count} odd numbers')