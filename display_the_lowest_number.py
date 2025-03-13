#display the lowest number

#sort
#print index 1

number_list = []

while True:
    try:
        user_input = int(input('Enteer a number: '))
        number_list.append(user_input)
        number_list.sort()
    except:
        print('error')
        break
        

print(number_list[0])