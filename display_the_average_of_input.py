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

#appended all the values to the list and used sum function for the total of all numbers
#divided it to the len which is the length or how many values is stored in the list