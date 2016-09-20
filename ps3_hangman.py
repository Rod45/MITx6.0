# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    len1 = len(secretWord)
    test = True
    for i in range(len1):
        if secretWord[i] not in lettersGuessed:
            test = False
            break
        else:
            i += 1
            
    return test 
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    len1 = len(secretWord)
    inProgress = ''
    for i in range(len1):
        if secretWord[i] in lettersGuessed:
            inProgress += secretWord[i]
            i += 1
        else:
            inProgress += '_'
            
    return inProgress 


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
    
    available = 'abcdefghijklmnopqrstuvwxyz'
    #len1 = len(lettersGuessed)
    availableList = []
    for letter in available:
        if letter not in lettersGuessed:
            availableList.append(letter)
    remaining = ''.join(availableList)
    return remaining
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!\nI am thinking of a word that is " + 
    str(len(secretWord)) +  "letters long.\n----------")
    lettersGuessed = ['']
    guesses = 8
    while (not (isWordGuessed (secretWord,lettersGuessed)) and guesses > 0):
        print("You have " + str(guesses) + " guesses left")
        print ("Available letters: "+ getAvailableLetters(lettersGuessed))
        userInput = input("Please guess a letter: ")
        if userInput in lettersGuessed:
            print("Oops! You've already guessed that letter: " 
            + getGuessedWord(secretWord,lettersGuessed))
        else:
            lettersGuessed.append(userInput)
            if userInput in secretWord:
                print("Good guess: "+getGuessedWord(secretWord,lettersGuessed))
            else:
                print("Oops! That letter is not in my word: " 
                + getGuessedWord(secretWord,lettersGuessed))
                guesses -= 1
        print("-----------")
    if guesses == 0:
        print("Sorry, you ran out of guesses, The word was " + secretWord)
    else:
        print("Congratulations, you won!")
                
        
        
        
    

'''
    code against duplicates
    1st incorrect guess regiistering as correct
    secretWord: The word to guess.
    lettersGuessed: The letters that have been guessed so far.
    mistakesMade: The number of incorrect guesses made so far.
    availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).

'''



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
