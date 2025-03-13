#print unique when entry does not have a duplicate
#  Display the number with the most number of duplicate.
# count numbers
# separate numbers with duplicates and those without 

initial_list = []
duplicate = []
no_duplicate = []
while True:
    try:
        user_input = int(input('Enter a number: '))
        initial_list.append(user_input)
        if user_input in initial_list:
            duplicate.append(user_input)
        if user_input not in duplicate:
            no_duplicate.append(user_input)
    except ValueError:
        print(no_duplicate)

        



  