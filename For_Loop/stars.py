stars = int(input("Max number of stars: ")) # Do not change this line


for i in range (stars + 1):
    i = "*" * i
    print(i)

for j in range (1, stars):
    j = stars - j
    print(j*"*")