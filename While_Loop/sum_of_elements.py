size_str = input("Please insert a positive number")
size_int = int(size_str)
number_list=[]
sum_of_list = 0

while size_int > 0:
    print("total sum is now:", sum_of_list)
    number_str = input("input a number")
    number_int = int(number_str)
    sum_of_list += number_int
    number_list.append(number_int)
    size_int -= 1
print(number_list)

