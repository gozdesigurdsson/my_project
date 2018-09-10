low = input ("Enter a lower bound")
high = input ("Enter a higher bound")

low_int = int(low)
high_int = int(high)

for number in range (low_int, high_int +1, 2):
    if number % 2 == 1:
        print(number)


