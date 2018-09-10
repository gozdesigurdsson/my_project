n = int(input("Input an int: ")) # Do not change this li

count = 1

while count <= n :
    if n % count == 0:
        print(count)
        count += 1
    else:
        count += 1
