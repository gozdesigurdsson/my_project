import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line
x1_int = int(x1_str) # convert strings to ints
y1_int = int(y1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)

#d = math.sqrt((y1_int - x1_int)**2 + (y2_int - x2_int)**2)

#print("d =",d)  # do not change this line

first_distance = x1_int - x2_int
second_distance= y1_int - y2_int

d= math.sqrt (first_distance**2 + second_distance**2)
print("d=" ,d)