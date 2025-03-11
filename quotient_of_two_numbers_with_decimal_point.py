#print quotient of two numbers

#ask user for two numbers
num_1 = float(input('Enter a number: '))
num_2 =float(input('Enter a number: '))

#operation
quotient = num_1 / num_2 
decimal_point = '.2f'
final_answer = f"{quotient,:{decimal_point}}"
print(final_answer)