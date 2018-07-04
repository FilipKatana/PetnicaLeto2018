#Modul Gameplay
import random
import Support as sup


def select_word(file_name):
    "Takes in file name without extension, and returns a selected word."
    f = open(file_name + ".txt", "r")
    candidates = f.read()
    selected = random.choice(candidates.split())
    return selected



def guess_character(selected_word, guessed_chars):
    "Prompts the user to make a guess"
    indexes = []
    char = input("Try and guess a character: ")
    char = char.lower()
    selected_word = selected_word.lower()
    if char in selected_word and not(char in guessed_chars):
        print("YOu guessed correctly!")
        indexes = sup.find_in_string(selected_word, char)
        return indexes, [char]
    elif char in guessed_chars:
        print("You already guessed that dummy")
        return [-2], []
    else:
        print("You guessed incorrectly ;(")
        return [-1], [char]


def show_word(word, known_indexes):
    "The function takes in a word and guessed indexes and displays progress on screen."
    for c in range(len(word)):

        if c in known_indexes:
            print(word[c], end = " ")
        else:
            print("", end = "_ ")
    print("")
            
def take_damage(lives):
    lives -= 1
    return lives

def show_lives(lives):
    print("You have " + str(lives) + " lives left.")


 

def draw_hangman(lives):
    if lives == 5:
        sup.draw("Lives 5.txt")
    if lives == 4:
        sup.draw("Lives 4.txt")

    if lives == 3:
        sup.draw("Lives 3.txt")

    if lives == 2:
        sup.draw("Lives 2.txt")

    if lives == 1:
        sup.draw("Lives 1.txt")


    


        

    
