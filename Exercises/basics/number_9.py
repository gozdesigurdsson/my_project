number_one = int(input("Please enter a number: "))
number_two = int(input("Please enter another number: "))
number_three = int(input("Please enter another number: "))

if number_one <= number_two <= number_three:
    print (number_one)
elif number_two <= number_one <= number_three:
    print(number_three)
elif number_three <= number_one <= number_two:
    print(number_three)
