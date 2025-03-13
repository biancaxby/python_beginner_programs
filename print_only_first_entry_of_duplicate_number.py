#display all numbers but for numbers with duplicates, only the first entry should be printed

users = []

for i in range (5):
    user_input = input('Enter a number: ')
    users.append(user_input)

new_list = [num for num in users if users.count < 1]

print(new_list)


