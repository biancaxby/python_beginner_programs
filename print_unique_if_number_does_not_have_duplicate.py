#print unique when entry does not have a duplicate
# count numbers
# separate numbers with duplicates and those without 


duplicate = []
no_duplicate = []
while True:
    try:
        user_input = int(input('Enter a number: '))
        no_duplicate.append(user_input)
    except ValueError:
        break

if user_input in no_duplicate:
    duplicate.append(no_duplicate)
    
print(f'These numbers are unique! {no_duplicate}')
        



  