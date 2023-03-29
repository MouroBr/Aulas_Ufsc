value = int(input())
count = 0

while count < 6:
    if value % 2 != 0:
        print(value)
        count += 1 
    
    value += 1
