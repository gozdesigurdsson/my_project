num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

if num1 > num2 and num1 > num3:
    max = num1
if num2 > num1 and num2 >num3:
    max = num2
if num3 > num1 and num3 > num2:
    max = num3
if num1 == num2 and num1 > num3:
    max = num1
if num2 == num3 and num2 > num1:
    max == num2
else:
    max == num3
   
print("The maximum is: ", max)# Do not change this line