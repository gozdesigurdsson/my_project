num = int(input("Input an int: ")) # Do not change this line

x = 1

count = 0

while count < num :
    if x % 2 == 0:
        x += 1
    else:
        print(x)
        x += 1
        count += 1


