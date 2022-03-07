

def getWord():
    word = input("Player 1, please enter a word: ")
    return  word.upper()

def play(word):
    wordCompletion = "_" * len(word)
    guessed = False
    lettersGuessed = []
    wordsGuessed = []
    tries = 6
    print("Lets Get Started")
    print(drawHangman(tries))
    print(wordCompletion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Player 2 Please enter your guess leeter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in lettersGuessed:
                print("You've already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                drawHangman(tries)
                lettersGuessed.append(guess)
            else:
                print("Yay,", guess, "is in the word!")
                lettersGuessed.append(guess)
                tries -= 1
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = "".join(wordAsList)
                if "_" not in wordCompletion:
                    guessed = True
                print(drawHangman(tries))
                print(wordCompletion)


        elif len(guess) == len(word) and guess.isalpha():
            if guess in wordsGuessed:
                print("You've already guessed this word", guess)
            elif guess !=word:
                print("Oops", guess, "is not the word")
                tries -= 1
                print(drawHangman(tries))
                print(wordCompletion)
                wordsGuessed.append(guess)
            else:
                print("Yay!! you guessed it right")
                guessed = True
                wordCompletion = word


        else:
            print("Not a valid Guess")
            print(drawHangman(tries))
            print(wordCompletion)
            print("\n")

    if guessed == True:
        print("Player 2 wins!!")
    else:
        print("Player 2 ran out of tries\n")
        print("the word was" + word)
        print("Player 1 Wins !!")






def drawHangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = getWord()
    play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        word = getWord()
        play(word)

if __name__ == "__main__":
    main()
