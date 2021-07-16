import random
print("Welcome to  'Can you Guese the Number'\n\n")
chances = 5

while True:
    computerNumber = random.randint(0, 9)
    try:
        userNumber = int(input("Please Enter the number you gussed\n"))
    
    except ValueError:
        print("Please enter number\n")
        userNumber = int(input("Please Enter the number you gussed\n"))

    if computerNumber == userNumber:
        print("Congratulations!!!  You Won the Game")
        break

    if not computerNumber == userNumber:
        if chances == 0:
            computer =  str(computerNumber)
            print("Sorry!!! You Lose ")
            print("The number is: "+ computer )
            break

        chances -= 1
        print("Try Again!!!\n")


