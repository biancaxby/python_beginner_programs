#Display the highest number

list = []

while True:
    try:
        user_input = int(input('Enter a number: '))
        if user_input:
            list.append(user_input)
    except ValueError:
        print('Invalid input')
        break

print(max(list))
