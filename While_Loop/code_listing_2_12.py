number_str = input("Please enter a number to check: ")
number_int = int(number_str)

divisor = 1
sum_of_divisors =  0

while divisor < number_int:
    if number_int % divisor == 0:
        sum_of_divisors = sum_of_divisors + divisor
    divisor = divisor + 1

if number_int == sum_of_divisors:
    print(number_int, "is perfect")
else:
    print(number_int, "is not perfect")
