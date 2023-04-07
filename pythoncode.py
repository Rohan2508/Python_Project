import random                                                                                 # import the library called random so that it will help to generate random number in a code

R_num = random.randint(1, 100)                                                                #R_num is assigned a random number between 1 and 100
G_num = 0                                                                                     #G_num is assigned as 0 so that number previous number is stored
guess_num = 0                                                                                 

while guess_num != R_num:                                                                     #using while loop, it will iterate till correct answer
    guess_num = input("Guess a number between 1 and 100: ")
    
    if guess_num == "quit":                                                                   #if user wants to quit from the game then enter -- quit
        print("you lost the challenge")
        break                                                                                 #this will break the loop and will come out of loop
    
    guess_num = int(guess_num)                                                                #converison into integer
    G_num = G_num + 1
    
    if guess_num < R_num:
        print("small number")
    elif guess_num > R_num:
        print("high number")
    else:
        print("success!you have guessed the correct number in", G_num, "guesses!")
