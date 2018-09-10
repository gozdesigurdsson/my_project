x = 1

while x <= 18 :
    par = input("Par of hole " + str(x) + ": ")
    score = input("Score on hole " + str(x) + ": ")
    par_int = int(par)
    score_int = int(score)

    if par_int - score_int == 0:
        print("par")

    elif par_int - score_int == -1:
        print("bogey")

    elif par_int - score_int == -2:
        print("double bogey")

    elif par_int - score_int == -3:
        print("triple bogey")
    
    elif par_int - score_int < -3:
        print("bad hole")

    elif par_int - score_int == 1:
        print("birdie")
    
    elif par_int - score_int == 2:
        print("eagle")

    elif par_int - score_int == 3:
        print("albatross")

    else:
        print("invalid score")
    
    
    x += 1

