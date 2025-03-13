#print unique when entry does not have a duplicate
# count numbers
# separate numbers with duplicates and those without 


duplicate = []
no_duplicate = []
while True:
    try:
        user_input = int(input('Enter a number: '))
        if user_input in no_duplicate:
                no_duplicate.remove(user_input)
                if user_input not in duplicate:
                     duplicate.append(user_input)
            
        if user_input not in duplicate:
            no_duplicate.append(user_input)
            
       
    except ValueError:
        print('Oops! Invalid number.')
        break

    
print(f'These numbers are unique! {no_duplicate}')
        



  