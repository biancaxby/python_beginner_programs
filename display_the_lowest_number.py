#display the lowest number

#sort
#print index 1

number_list = []

while True:
    try:
        user_input = int(input('Enteer a number: '))
        number_list.append(user_input)
        
    except:
        print('error')
        break
        
h = number_list.sort
print(h[1])