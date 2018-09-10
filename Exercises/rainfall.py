inches_str  = input("how many inches of rain have fallen? ")
inches_int = int(inches_str)

volume = (inches_int/12) * 43560
print (volume)

gallons = volume * 7,48051945
print (gallons)

print(inches_int, "in. rain on 1 acre is" , gallons, "gallons" )






