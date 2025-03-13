#display all numbers that dont have a duplicate
users = []

# ask user for numbers
for i in range(10):
    user = input("Enter a number: ")
    users.append(user)

# Filter out numbers that have duplicates
no_duplicate = [num for num in users if users.count(num) == 1]

print("Numbers without duplicates:", no_duplicate)