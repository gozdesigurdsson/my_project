grade = float(input("Input a grade: ")) # Do not change this line

if grade < 0.0 :
    print("Invalid grade!")
elif 10.0 >= grade >= 5.0 :
    print("Passing grade!")
else:
    print("Failing grade!")
