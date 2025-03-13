#display the lowest number

#sort
#print index 0

number_list = []

while True:
    try:
        user_input = int(input('Enter a number: '))
        number_list.append(user_input)
        number_list.sort()
    except:
        print('Error. Invalid input')   
        break
        

print('The lowest number is', number_list[0])
