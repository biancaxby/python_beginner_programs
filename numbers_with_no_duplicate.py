#display all numbers that dont have a duplicate

num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter a number: '))
num_3 = int(input('Enter a number: '))
num_4 = int(input('Enter a number: '))
num_5 = int(input('Enter a number: '))
num_6 = int(input('Enter a number: '))
num_7 = int(input('Enter a number: '))
num_8 = int(input('Enter a number: '))
num_9 = int(input('Enter a number: '))
num_10 = int(input('Enter a number: '))

if num_1 ==  num_2 or num_1 == num_3 or num_1 == num_4 or num_1 == num_5 or num_1 == num_6 or num_1 == num_7:
    print(  num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10)
elif num_2 == num_1 or num_2 == num_2 or num_2 == num_3 or num_2 == num_4 or num_2 == num_5 or num_2 == num_6 or num_2 == num_7 or num_2 == num_8 or num_2 == num_9 or num_2 == num_10:
    print(num_1, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10)
elif num_3 == num_1 or num_3 == num_2 or num_3 == num_3 or num_3 == num_4 or num_3 == num_5 or num_3 == num_6 or num_3 == num_7 or num_3 == num_8 or num_3 == num_9 or num_3 == num_10:
    print(num_1, num_2, num_4, num_5, num_6, num_7, num_8, num_9, num_10)
elif  num_3 == num_1 or  num_3 == num_2 or num_3 == num_3 or num_3 == num_4 or num_3 == num_5 or num_3 == num_6 or num_3 == num_7 or num_3 == num_8 or  num_3 == num_9 or num_3 == num_10:
    print(num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10)
elif  num_4 == num_1 or  num_4 == num_2 or num_4 == num_3 or num_4 == num_4 or num_4 == num_5 or num_4 == num_6 or num_4 == num_7 or num_4 == num_8 or num_4 == num_9 or num_4 == num_10:
    print(num_1, num_2, num_3, num_5, num_6, num_7, num_8, num_9, num_10)
elif num_5 == num_1 or  num_5 == num_2 or num_5 == num_3 or num_5 == num_4 or num_5 == num_5 or num_5 == num_6 or num_5 == num_7 or num_5 == num_8 or num_5 == num_9 or num_5 == num_10:
    print((num_1, num_2, num_3, num_4, num_6, num_7, num_8, num_9, num_10))
elif  num_6 == num_1 or  num_6 == num_2 or num_6 == num_3 or num_6 == num_4 or num_6 == num_5 or num_6 == num_6 or num_6 == num_7 or num_6 == num_8 or num_6 == num_9 or num_6 == num_10:
    print((num_1, num_2, num_3, num_4, num_5, num_7, num_8, num_9, num_10))
elif  num_7 == num_1 or  num_7 == num_2 or num_7 == num_3 or num_7 == num_4 or num_7 == num_5 or num_7 == num_6 or num_7 == num_7 or num_7 == num_8 or num_7 == num_9 or num_7 == num_10:
    print((num_1, num_2, num_3, num_4, num_5, num_6, num_8, num_9, num_10))
    
    
    
else: 
    print('hatdog')