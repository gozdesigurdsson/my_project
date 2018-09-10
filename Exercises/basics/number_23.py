low = int(input("Enter: "))
high = int(input("Enter: "))

total = 0

for i in range(low,high+2):
    if i%2 == 1 :
        total += i
        print( total )
    