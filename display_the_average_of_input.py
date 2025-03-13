#Display the average

number_list = []

while True:
    try:
        numbers = int(input('Enter a number: '))
        number_list.append(numbers)
    
    except ValueError:
        print('Error')
        break


average = sum(number_list) / len(number_list)
print(average)



