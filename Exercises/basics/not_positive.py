count = 0

while True:
    number = int(input("Please insert a number: "))
    if number < 0:
        number == abs(number)
        count = count + 1
    else:
        break