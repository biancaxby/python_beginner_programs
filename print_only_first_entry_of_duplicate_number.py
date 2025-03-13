#display all numbers but for numbers with duplicates, only the first entry should be printed

users = []
users_2 = []
for i in range (5):
    user_input = int(input('Enter a number: '))
    if user_input in users:
        users_2.append(user_input)
    else:
        users.append(user_input)
     





print(users)


