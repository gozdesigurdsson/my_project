n = int(input("Input a natural number: ")) # Do not change this line

count = 2

while count <= n:
    print(count)
    if n == count:
        prime = True
    elif n % count == 0 :
        prime = False
        break

    count += 1

if prime:
    print("Prime")
else:
    print("!Prime")