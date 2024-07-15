import random
"""this function starts to play a game"""
lifes = 0
playing_game = True




print ('Hello welcome to the guess the number game! it is between 1 to 100')
diffculty = input('what diffculty do you want to select ? "Easy" or "Hard" ')

if diffculty == "Hard":
    lifes += 5
elif diffculty == "Easy":
    lifes += 10
else:
    print('the first letter is always capatial.')
    exit()
number = random.randint(0,100)
print("you have ",lifes, "lifes left")
while playing_game == True:    
    def check_number():
            global lifes
            guess = int(input('what is your guess: '))
            if number - guess < 0 :
                print ('too high')
                lifes -= 1
            elif number - guess == 0 :
                print ('You Won!')
                exit()
            elif number - guess >= 0 :
                print('Too Low')
                lifes -= 1
            print("you have ",lifes, "lifes left")
    if playing_game == True:
        check_number() 
    if lifes == 0:
        print("You Lost")
        print("thanks for playing the final number was ",number)
        playing_game = False
    if playing_game == False:
        x = input ("Do you what to play again if yes then type 'yes' if no then type 'no'")
        if x == "yes":
            playing_game = True
        elif x == "no":
            playing_game = False
            exit()


    
