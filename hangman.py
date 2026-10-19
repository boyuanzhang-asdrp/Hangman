import random

playAgain = "yes"

while playAgain.lower() == "yes":
    
    livesLeft = 6
    wordFile = open("words.txt", "r")
    wordList = wordFile.read().splitlines()
    word = random.choice(wordList).lower()
    guessedWord = []
    correctWord = list(word)

    numLetters = len(word)

    for _ in range(len(word)):
        guessedWord.append("_")


    while (guessedWord != correctWord and livesLeft > 0):
        print(*guessedWord)
        guess = input(f"Lives left: {livesLeft} \n Guess a letter: ")
        guess = guess.lower()

        while (guess.isnumeric() or len(guess) > 1):
            guess = input("Not a valid guess. try again:")

        i=0
        found = False
        for i in range(len(word)):
            if(correctWord[i] == guess ):
                guessedWord[i] = guess
                found = True
        if found == False:
            livesLeft -= 1

    if livesLeft > 0:
        print ("You win!")
    else:
        print("You ran out of lives and lost")

    playAgain = input("Do you want to play again? (Yes/No) ")
    


