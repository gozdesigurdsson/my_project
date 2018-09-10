def area_of_rectangle (a,b):
    result = a * b
    return result

lenght = input ("Please insert the lenght")
height = input ("Please insert the height")

lenght_int = int(lenght)
height_int = int(height)

x = area_of_rectangle (lenght_int, height_int)
print(x)