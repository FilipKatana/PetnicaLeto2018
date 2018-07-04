#MAIN
import Gameplay as game
import Support as sup
import time


selected_word = game.select_word("Candidates")
lives = 5
indexes = []
temp = []
guessed = 0
guessed_chars = []
g_temp = []

while lives > 0:
    if guessed == len("".join(set(selected_word))):
        print("YAAAY! You win!")
        break
    time.sleep(0.6)
    game.draw_hangman(lives)
    game.show_word(selected_word, indexes)
    game.show_lives(lives)
    temp, g_temp = game.guess_character(selected_word, guessed_chars)
    if temp == [-1]:
        lives = game.take_damage(lives)
        continue
    if temp == [-2]:
        continue

    indexes = sup.unite(indexes, temp)
    guessed_chars = sup.unite(guessed_chars, g_temp)
    guessed += 1


if lives <= 0:
    print("Booo you suck...")
    
    
        
        
    
    
