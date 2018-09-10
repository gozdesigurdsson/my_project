low = input("please input the lower bound")
high = input("please input the higher bound")

low_int = int(low)
high_int = int(high)

counter = low_int

while counter <= high_int:
    if counter % 2 == 1:
        print(counter)
    counter += 1


