import random
option=[1,2,3,4,5,6]

bowls= 20
no_of_chances= 0
your_runs= 0
comp_runs= 0

print("   You   = ODD ")
print("Computer = EVEN")

User=int(input("Enter Your Choice 1 to 6 = "))
comp=int(random.choice(option))
print("Computer Choose Random Number is =",comp)

Toss_decision=User+comp
print("Sum is = ",Toss_decision)

if Toss_decision%2==0:
    print("Toss Decision = EVEN")
    print("--COMPUTER WON THE TOSS--")
    print("Computer Choose Batting....")
    print ("-----------------------------------------------")
    print ("Computer Batting-\n")
    while no_of_chances < bowls:
        bowl=int(input("Enter Runs For Your Bowling = "))
        comp_bat=random.choice(option)

        if comp_bat==bowl:
            print("Computer Guess: ",comp_bat,"Your Guess = ",bowl)
            print ("The Computer is Out. Computer Runs = ",comp_runs,"\n")
            break
        elif bowl > 6 :
            print("ALERT!! Support No only till 6")
            continue
        else :
            comp_runs = comp_runs+comp_bat
            print ("Computer Guess = ",comp_bat,"Your Guess = ",bowl)
            print ("Computer Runs = ",comp_runs,"\n")

        no_of_chances= no_of_chances+1
    
    print ("-----------------------------------------------\nYour Batting\n")
    while no_of_chances < bowls:
        runs=int(input("Enter Runs for Your Batting Turn = "))
        comp_bowl= int(random.choice(option))
        if runs==comp_bowl:
            print ("Your Guess = ",runs,",Computer Guess = ",comp_bowl)
            print ("You are Out. Your Total Runs = ", your_runs,"\n")
            break
        elif runs > 6:
            print ("ALERT!! Support No only till 6\n")
            continue
        else :
            your_runs= your_runs+runs
            print ("Your Guess = ",runs,",Computer Guess = ",comp_bowl)
            print ("Your runs Now are = ",your_runs,"\n")

        no_of_chances = no_of_chances + 1
else :
    print("Toss Decision = ODD")
    print("--YOU WON THE TOSS--")
    print("NOTE :- Don't make spelling mistakes when you enter your choice")
    User_Choice=input("Enter Your Choice Batting Or Bolling :")
    if User_Choice=='Batting':
        print ("-----------------------------------------------\nYour Batting\n")
        while no_of_chances < bowls:
            runs= int(input("Enter Runs for Your Batting Turn = "))
            comp_bowl= random.choice(option)
            if runs==comp_bowl:
                print ("Your Guess = ",runs,",Computer Guess = ",comp_bowl)
                print ("You are Out. Your Total Runs = ", your_runs,"\n")
                break
            elif runs > 6:
                print ("ALERT!! Support No only till 6\n")
                continue
            else :
                your_runs= your_runs+runs
                print ("Your Guess = ",runs,",Computer Guess = ",comp_bowl)
                print ("Your runs Now are = ",your_runs,"\n")

            no_of_chances = no_of_chances + 1  

        print ("-----------------------------------------------")
        print ("Computer Batting-\n")
        while no_of_chances< bowls:
            bowl= int(input("Enter Runs for Your Bowling Turn = "))
            comp_bat= int(random.choice(option))
            if comp_bat==bowl:
                print ("Computer Guess = ",comp_bat,"Your Guess = ",bowl)
                print ("The Computer is Out. Computer Runs = ",comp_runs,"\n")
                break
            elif bowl > 6:
                print("ALERT!! Support No only till 6")
                continue
            else:
                comp_runs = comp_runs+comp_bat
                print ("Computer Guess = ",comp_bat,"Your Guess = ",bowl)
                print ("Computer Runs = ",comp_runs,"\n")

            no_of_chances= no_of_chances+1

    else:
        print("You Choose The Bolling...")
        print ("-----------------------------------------------")
        print ("Computer Batting-\n")
        while no_of_chances< bowls:
            bowl= int(input("Enter Runs for Your Bowling Turn  = "))
            comp_bat= int(random.choice(option))
            if comp_bat==bowl:
                print ("Computer Guess = ",comp_bat,"Your Guess = ",bowl)
                print ("The Computer is Out. Computer Runs = ",comp_runs,"\n")
                break
            elif bowl > 6:
                print("ALERT!! Support No only till 6")
                continue
            else:
                comp_runs = comp_runs+comp_bat
                print ("Computer Guess = ",comp_bat,"Your Guess = ",bowl)
                print ("Computer Runs = ",comp_runs,"\n")

            no_of_chances= no_of_chances+1
        
        print ("-----------------------------------------------\nYour Batting\n")
        while no_of_chances < bowls:
            runs= int(input("Enter Runs for Your Batting Turn = "))
            comp_bowl= random.choice(option)
            if runs==comp_bowl:
                print ("Your Guess = ",runs,",Computer Guess = ",comp_bowl)
                print ("You are Out. Your Total Runs = ", your_runs,"\n")
                break
            elif runs>6:
                print ("ALERT!! Support No only till 6\n")
                continue
            else :
                your_runs= your_runs+runs
                print ("Your Guess = ",runs,",Computer Guess = ",comp_bowl)
                print ("Your runs Now are = ",your_runs,"\n")

            no_of_chances = no_of_chances + 1 
next

print ("\n-----------------------------------------------\nRESULTS: \n")
print("Computer Total Runs =",comp_runs)
print(" Your  Total  Runs  =",your_runs)
if comp_runs < your_runs:
    print("---YOU WON THE GAME---")
elif comp_runs == your_runs:
    print("---GAME IS TIE---")
else:
    print("---COMPUTER WON THE GAME---")  