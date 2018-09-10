low = int(input("Input:" ))
high = int(input("Input: "))

total = 0

for i in range(low,high+1):
    if (i % 3 == 0) and (i % 5 == 0) :
        total += i
        print(total)