#=========================== Number Guess =======================
print("#=========================== Number Guess =======================")
print("Welcome to Number Guess with QIBLI! (please watch Carol of the QIBLI on youtbe it awesoome- Qibli)! You are going to guess my number in between 1 to 50! You have unlimited guess! Good Luck- Qibli")
print("NUMBER NUMBER WHICH NUMBER ONMIOUS MYSTICAL TALK MWA HA HA HA HA O WHATEVER- Qibli")
import random
Number= random.randint(1,50)
playing=True
while playing:
    print("INTIALISING SEQUENCE 5,4,3,2,1 Go Go Go!")
    Guess= int(input("Enter your  guess: "))
    if Guess == Number:
        print("CONGRATS WELL DONE AND HUZZAH AND YAY YAY YAY YAY ON GUESSING RIGHT!")
        playing=False
    else:
        print("Wrong answer try again!")

print("Bye! See you at the MOONS also  maaaaaaaaybe at JMA!")