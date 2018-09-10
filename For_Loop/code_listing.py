river = "Mississippi"
target = input("Please input a character to find: ")

for index in range(len(river)):
    if river[index] == target:
        print("Letter found at index: ", index)
        break
else:
    print("Letter" , target, "not found", river)
