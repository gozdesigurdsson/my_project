size_str = input("Please insert a positive number")
size_int = int(size_str)
number_list = []

for x in range (size_int):
    number = input("Please enter a number")
    number_int = int(number)
    number_list.append(number)

print(number_list)


