size_str = input ("Please input a size")
size_int = int(size_str)
number_list= []

for x in range(size_int):
    number_str = input ("Please enter a number")
    number_int = int(number_str)
    number_list.append(number_int)
print(number_list)

for number in number_list:
    total += number

average = total / size_int

print(average)