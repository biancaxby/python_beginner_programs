#display all numbers but for numbers with duplicates, only the first entry should be printed


# add two list
users = []
users_2 = []

# all the values that were added should be appended to users list. but if the value is already there, it should be appended to users_2
#since they are separated, i can only print one of the lists

for i in range (10):
    user_input = int(input('Enter a number: '))
    if user_input in users:
        users_2.append(user_input)
    else:
        users.append(user_input)
    

print(users)


