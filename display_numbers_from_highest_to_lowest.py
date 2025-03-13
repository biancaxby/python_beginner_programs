#Display the number from highest to lowest

lists = []

while True:
    try:
        user_input = int(input('Enter a number: '))
        
        if user_input:
            lists.append(user_input)
            lists.sort(reverse=True)

    except ValueError:
        print('Invalid input')
        break

print(lists)