#Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.


no_duplicates = []
duplicates = []

for i in range(10):
        user_input = int(input('Enter a number: '))
        if user_input in no_duplicates:
            duplicates.append(user_input)
        if user_input not in duplicates:    
            no_duplicates.append(user_input)
              

print(duplicates)
