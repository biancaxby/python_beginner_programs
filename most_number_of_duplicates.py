#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

no_duplicate = []
duplicate = []

while True:
    try:
        user_input = int(input('Enter a number: '))
        if user_input in no_duplicate:
            duplicate.append(user_input)
        else:
            no_duplicate.append(user_input)

    except ValueError:
        if duplicate:
            duplicates = max(set(duplicate), key=duplicate.count)
            print(f'The most duplicate numbers is {duplicates}')