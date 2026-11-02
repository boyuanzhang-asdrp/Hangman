import random

playAgain = "yes"

while playAgain.lower() == "yes":
    print("Lets play Hangman!")
    
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

        while (guess.isnumeric() or len(guess) > 1 or not guess.isalpha()):
            guess = input("Not a valid guess. try again:").lower()

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
        print("The word was:", word)

    playAgain = input("Do you want to play again? (Yes/No) ")
    while(playAgain.lower() != "yes" and playAgain.lower() != "no"):
        playAgain = input("Not a valid response, Yes/No: ")

print("Thank you for playing!")