num = int(input("Input an int: ")) # Do not change this line

for i in range (0, num):
    if i < 10:
        armstrong = i**1
        if armstrong == i:
            print(armstrong)

    elif 1000 > i > 99:
        armstrong = (i // 100)** 3 + (i // 10 % 10)**3 + (i % 10)**3
        if armstrong == i:
            print(armstrong)


#n = 153

#print(n // 100)
#print(n // 10)
#print(n % 10)
#print(n // 10 % 10)






