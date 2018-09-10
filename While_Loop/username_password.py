defuser = "flower"
defpassword = "1234"

while True:
    user = input("Please write your username: ")
    password  = input("Please write your password: ")
    if (defuser == user) and (defpassword == password):
        print("Welcome ", user)
        break
    elif (defuser != user) and (defpassword == password):
        print("Incorrect username")
    elif (defuser == user) and (defpassword != password):
        print("Incorrect password")
        print("Would you like to change your password? (Y/N)")

        answer = input()
        if answer == "Y":
            newpassword = input("Please enter your new password: ")
            defpassword == newpassword
    else:
        print("Please try again")

