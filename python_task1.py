from random import *
from copy import *
ch = int(input("Do you want to play the MASTERMIND GAME?\n1 - Yes\n0 - No\n"))
while ch == 1:
    ran, score = randint(1000, 9999), 40
    rlst, ng = [int(i) for i in str(ran)], 10
    while ng > 0:
        tlst, cdcp, cdwp, cg = deepcopy(rlst), [], [], 0
        guess = int(input("Guess the number : "))
        glst = [int(i) for i in str(guess)]
        for i in range(0, 4):
            if glst[i] in tlst:
                if glst[i] == rlst[i]:
                    cdcp.append(glst[i])
                    cg += 1
                else:
                    cdwp.append(glst[i])
                tlst[tlst.index(glst[i])] = -35487
            else:
                score -= 2
        print(len(cdcp), " correct digits at correct position: ", cdcp)
        print(len(cdwp), " correct digits at wrong position ", cdwp)
        ng -= 1
        if cg == 4:
            print("Congratulations you have guessed the number correctly. You won the game.\n")
            break
        else:
            print("Sorry, guess again.\nGuesses left : ", ng)
    print("Your score is : ", score)
    ch = int(input("You have finished the game. Do you want to play again?\n1 - Yes\n0 - No\n"))
