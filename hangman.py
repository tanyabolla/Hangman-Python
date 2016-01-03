#!C:\Python27\python.exe
#Hangman
from __future__ import print_function
import random
import sys

'''program cannot substitute if there are multiple same letters in a word'''
#rest of the program works

FIRST_TRY = '''    0 '''
SECOND_TRY = '''    0
    | '''
THIRD_TRY = '''    0
    |
    | '''
FOURTH_TRY = '''    0
   \|
    | '''
FIFTH_TRY = '''    0
   \|/
    | '''
SIXTH_TRY = '''    0
   \|/
    |
   / '''
GAME_OVER = '''    0
   \|/
    |
   / \ '''
GUESSED_LETTERS = []
LETTERS_NOT_IN_WORD = []
ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z']

def welcome():
    print("Welcome to Hangman. You get seven chances to guess the mystery word.")

def randomWord():
    '''chooses a random word from the file words.txt'''
    wordLocation = random.randint(0, 100)
    inputFile = open("words.txt", "r")
    for i in range(wordLocation):
        word1 = inputFile.readline()
        word = word1.strip('\n')
    print(word)
    inputFile.close()
    return word

def printSpaces(word):
    '''inputs the word into a list and creats dashes on the screen according to the
    numbers of characters in the word'''
    dashList = []
    wordList = []
    for i in range(len(word)):
        print("- ", end = '')
    for i in word:
        dashList.append('-')
    for i in word:
        wordList.append(i)
    return dashList, wordList

def inputLetter():
    '''asks the user for an input. Checks to see if it's a letter. Then, checks if the
    letter has already been guessed. If it passes these checks, then the letter is inputted
    into the list of guessed letters'''
    letter = raw_input("\nPick a letter: ").lower()
    while letter not in ALPHABET:
        print("That's not a letter!! Try again!")
        letter = raw_input("\nPick a letter: ").lower()
    if letter in GUESSED_LETTERS:
        print("Sorry, you already guessed", letter)
    else:
        for i in letter:
            GUESSED_LETTERS.append(i)
    print('Guessed letters:', ', '.join(GUESSED_LETTERS))
    return letter

def checkLetter(word, letter, wordList, dashList):
    '''Checks if the letter is in the alphabet and if it is, it checks to see if the letter
    is in the word, and if it the letter isn't in the word, it prints the hangman'''
    while letter in ALPHABET:
        for element in GUESSED_LETTERS:
            if element not in wordList:
                LETTERS_NOT_IN_WORD.append(element)
        noDup = list(set(LETTERS_NOT_IN_WORD))
        if letter in word:
            dashList[wordList.index(letter)] = letter
            print(' '.join(dashList))
            wholeWord(word, letter, wordList, dashList)
            #program crashes here if there are repeat letters in a word
            if(dashList != wordList):
                letter = inputLetter()
            else:
                break
        else:
            print(' '.join(dashList))
            if len(noDup) == 1:
                print(FIRST_TRY)
                letter = inputLetter()
            elif len(noDup) == 2:
                print(SECOND_TRY)
                letter = inputLetter()
            elif len(noDup) == 3:
                print(THIRD_TRY)
                letter = inputLetter()
            elif len(noDup) == 4:
                print(FOURTH_TRY)
                letter = inputLetter()
            elif len(noDup) == 5:
                print(FIFTH_TRY)
                letter = inputLetter()
            elif len(noDup) == 6:
                print(SIXTH_TRY)
                letter = inputLetter()
            elif len(noDup) == 7:
                print(GAME_OVER)
                print("Game over! You didn't guess the word.")
                print("The mystery word was", word)
                for letter in word:
                    dashList[wordList.index(letter)] = letter
                del noDup[:]
                del GUESSED_LETTERS[:]
                del LETTERS_NOT_IN_WORD[:]
                break
            
def wholeWord(word, letter, wordList, dashList):
    '''asks the user whether he would like to guess the whole word'''
    inputWord = raw_input("Would you like to guess the whole word? Y for yes, N for no: ").lower()
    while inputWord == 'y':
        giveWord = raw_input("What's the word?: ")
        if giveWord == word:
            for letter in word:
                dashList[wordList.index(letter)] = letter
            print(' '.join(dashList))
            print("Congratulations! That's the correct word!")
            break
        else:
            print("Sorry, that's the wrong word!")
            print("Game Over!")
            break
    
def playGame():
    word = randomWord()
    dashList, wordList = printSpaces(word)
    while(dashList != wordList):
        letter = inputLetter()
        checkLetter(word, letter, wordList, dashList)
        print("Play Again!")
        word = randomWord()
        dashList, wordList = printSpaces(word)
    
def main():
    welcome()
    while True:
        playGame()

main()

