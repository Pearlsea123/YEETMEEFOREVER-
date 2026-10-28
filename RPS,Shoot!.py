#============= Rock Paper Scissors Shoot! ! also maybe YEET ME! ================
print("============= Rock Paper Scissors Shoot! ! also maybe YEET ME! ================")
print("HIimKinkajouandI'm3andMoonTellsMeNotToSAYALLOfThsiSoWeArePlayingAGameNoMoonSaysBYEEEEEEEEE - Kinkajou")
print("Here we goooooooo")
import random


Playing= True
while Playing:
    Shoot1= random.randint(1,3)
    if Shoot1 == 1:
        Shoot2Comp= "Paper"
    elif Shoot1 == 2:
        Shoot2Comp= "Scissors"
    else:
        Shoot2Comp= "Rock"
    Player= input("Rock,Paper,Scissors,SHOOT: ")
    print("I played: ",Shoot2Comp)
    if Player == Shoot2Comp:
        print("its a Tie!")
    elif Player == "Paper" and Shoot2Comp == "Rock":
        print("You Win!")
    elif Player == "Rock" and Shoot2Comp == "Scissors":
        print("You Win!!")
    elif Player == "Paper" and Shoot2Comp == "Scissors":
        print("Good Try !")
    elif Shoot2Comp == "Paper" and Player == "Rock":
        print("Good Try")
    elif Shoot2Comp == "Rock" and Player == "Scissors":
        print("Good Try!")
    elif Shoot2Comp== "Paper" and Player == "Scissors":
        print(" You Win!")
    Plays= input("Do you want to play again: ")  
    if Plays == "No":
        Playing= False
