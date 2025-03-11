#print all numbers from 0-100 except numbers ending in zero or five

#for loop will print numbers in a specific range 
for i in range(0,100):
    if i %5 != 0:
        print(i)