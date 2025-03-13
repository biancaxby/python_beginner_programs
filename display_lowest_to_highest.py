#lowest to highest number

# initialize list
number_list = []

while True:
    try:
        user_input = int(input('Enter a number: '))
        number_list.append(user_input) # adds the numbers in the list
        number_list.sort()  # sorts out the value
    except:
        print('Error. Invalid input')   
        break
        
print(number_list)