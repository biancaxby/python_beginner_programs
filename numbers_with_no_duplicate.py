#display all numbers that dont have a duplicate

num = 0
while num <= 10:
    num = int(input('Enter a number: '))
    if num == num:
        num.remove(num)
        
    if num != num:
        print(num)
        break

    






