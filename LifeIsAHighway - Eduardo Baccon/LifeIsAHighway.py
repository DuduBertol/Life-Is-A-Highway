from random import randint
from time import sleep
import os
import Frames

# ========================================

language = {"English": 1, "Portuguese": 2}
languageSelected = 0

portugueseWordBank = ["Toy+Story", "Monstros+S+A", "Procurando+Nemo", "Os+Incriveis", "Carros",  "Ratatui",
             "WALL+E", "Up+Altas+Aventuras", "Divertidamente", "Procurando+Dory", "Viva+A+Vida+E+Uma+Festa", "Elementos"]
englishWordBank = ["Toy+Story", "Monsters+Inc", "Finding+Nemo", "The+Incredibles", "Cars",  "Ratatouille",
             "WALL+E", "Up", "Inside+Out", "Finding+Dory", "Coco", "Elements"]
wordsBank = []

englishStory = (f"""
{"===================================================":^80}
{"Ka-Chow!":^80}
{"McQueen is on his last lap of the Piston Cup!":^80}

{"To win the race, he needs to perform a risky jump!":^80}
{"Help him complete the jump!":^80}

{"Be careful! The spikes on the ground are dangerous!":^80}

{">> Choose a letter! <<":^80}
{">> You have 5 guesses to guess the name of PIXAR MOVIES! <<":^80}

{"===================================================":^80}

{">> START <<":^80}

""")
portugueseStory = (f"""
{"===================================================":^80}
{"Ka-Chow!":^80}
{"McQueen está na sua última volta da Copa Pistão!":^80}

{"Para vencer a corrida, ele precisa realizar um salto arriscado!":^80}
{"Ajude-o a completar o salto!":^80}

{"Tome cuidado! Os espinhos do chão são perigosos!":^80}

{">> Escolha uma letra! <<":^80}
{">> Você tem 5 palpites para adivinhar o nome dos FILMES DA PIXAR! <<":^80}

{"===================================================":^80}

{">> INICIAR <<":^80}

""")
story = [englishStory, portugueseStory]

charInputText = ["Type your guess", "Digite seu palpite"]
lifeText = ["LIFES", "VIDAS"]
letterHistoryText = ["LETTERS", "LETRAS"]
wordText = ["MOVIE", "FILME"]

displayMessageText = ""
rightText = ["You got it right!", "Você acertou!"]
repeatedText = ["Repeated Letter!", "Letra repetida!"]
wrongText = ["You miss!", "Você errou!"]


englishEndGameWords = {"End": "THE END.", "Movie": "MOVIE", "Tries": "TRIES", "Percent": "PERCENT COMPLETED", "Attempt": "GUESS"}
portugueseEndGameWords = {"End": "O FIM.", "Movie": "FILME", "Tries": "TENTATIVAS", "Percent": "PORCENTAGEM COMPLETA", "Attempt": "PALPITE"}
endGameWords = [englishEndGameWords, portugueseEndGameWords]

randomWord = ""
wordLenght = 0
wordToComplete = []
wordsToDiscover = 0
letterHistory = []

isGameOver = False
isGameWinner = False

lifes = 5
percent = 0
strPercent = ""



# descubro o percentual por meio da quantidade de "_" restantes

# tryValue = (10/total) / total

# FUNCTIONS ==============================================================================================

def language_selection():
    print()
    print(f"{'>> ENTER TO PLAY <<':^70}")
    input(" ")

    print("Select your language:")
    print("-> [1] English")
    print("-> [2] Portuguese")

    selection = int(input(">> "))

    global languageSelected, wordsBank, story

    if selection == language["English"]:
        languageSelected = language["English"]-1
        wordsBank = englishWordBank


    elif selection == language["Portuguese"]:
        languageSelected = language["Portuguese"]-1
        wordsBank = portugueseWordBank

def tell_story():
    global languageSelected

    sleep(0.25)
    os.system("cls")
    Frames.start_frame()
    print()
    input(story[languageSelected])


def start():
    os.system("cls")

    global randomWord, wordLenght, wordToComplete, wordsToDiscover

    Frames.start_frame()
    language_selection()
    tell_story()

    randomWord = wordsBank[randint(0, len(wordsBank) - 1)]
    wordLenght = len(randomWord)
    wordToComplete = ["_"] * len(randomWord)
    wordsToDiscover = wordLenght - randomWord.count("+")

    for i, letter in enumerate(randomWord):
        if letter in "+":
            wordToComplete[i] = " "



def gameplay_loop():
    print()
    print("="*50)

    print(f"\n >> {displayMessageText}")

    print(f"\n{wordText[languageSelected]} >> ", end="")
    for l in wordToComplete:
        print(l, end="")

    print(f"\n{letterHistoryText[languageSelected]} >> ", end="")
    for l in letterHistory:
        print(l, end="")

    print(f"\n{lifeText[languageSelected]} >> {lifes}")
    print()
    charTry = (input(f"{charInputText[languageSelected]}: >> ")).split()[0]
    letterHistory.append(charTry.split()[0].upper())
    word_check(charTry)

def word_check(char):
    global wordsToDiscover
    timesFinded = 0
    repeatedLetter = False

    for i, letter in enumerate(randomWord):
        tempLetter = letter
        tempChar = char
        if tempChar.lower() == tempLetter.lower():
            timesFinded += 1
            if wordToComplete[i] != letter:
                wordToComplete[i] = letter
                wordsToDiscover -= 1
                repeatedLetter = False
            else:
                repeatedLetter = True

    info_check(timesFinded, repeatedLetter)

def info_check(times_finded, repeated_letter):
    global lifes, percent, strPercent
    global displayMessageText
    global isGameOver, isGameWinner

    #LIFE
    if times_finded <= 0:
        lifes -= 1
        displayMessageText = wrongText[languageSelected]
    else:
        if repeated_letter:
            displayMessageText = repeatedText[languageSelected]
        else:
            displayMessageText = rightText[languageSelected]

    #PERCENT
    percent = 10*((len(randomWord) - randomWord.count("+") - wordsToDiscover ) / (len(randomWord) - randomWord.count("+")))
    strPercent = f"{int(percent * 10)}%"

    #GAME
    if lifes <= 0:
        isGameOver = True
    if percent >= 10:
        isGameWinner = True

# PRINTS ==============================================================================================

def print_car():
    multiplier = 10 * (10 - int(percent))
    space = " " * multiplier
    saved_space = " " * 5

    if not isGameOver:
        print_above_spaces()
        print(f"{space}{saved_space}        ________      ")
    print(f"{space}{saved_space}   ____/(0)  |\\ \\____/ ")
    print(f"{space}{saved_space}  /) _    z95z _    |     ")
    print(f"{space}{saved_space} /__/ \\_______/ \\__/   ")
    if not isGameOver: print(f"{space}{saved_space}    \\_/       \\_/      ")

def print_above_spaces():
    for i in range(5-lifes):
        print()

def print_below_spaces():
    for i in range(lifes):
        print()

def print_ground():
    print(("_"* 30) + ("/\\" * 50))


def print_winner():
    saved_space = " " * 5
    for i in range(4):
        print()
    print(f"{saved_space}        ________        {saved_space}/    {saved_space}/    ")
    print(f"{saved_space}   ____/(0)  |\\ \\____/{saved_space} /__ {saved_space} /__ ")
    print(f"{saved_space}  /) _    z95z _    |   {saved_space} /   {saved_space} /   ")
    print(f"{saved_space} /__/ \\_______/ \\__/  {saved_space}  /  {saved_space}  /   ")
    print(f"{saved_space}    \\_/       \\_/                                         ")
    print(("_" * 30) + ("/\\" * 50))
    print()
    print("="*50)
    print(f"{'YOU ARE A WINNER!':^50}")
    print(f"{'=======================':^50}")
    print(f"{'KA-CHOW!':^50}")
    print(f"{'=======================':^50}")

    print(f"{'McQUENN HAS LANDED SAFELY!':^50}")
    print("="*50)
    print()


def print_kaboom():
    if isGameOver:
        multiplier = 10 * (10 - int(percent))
        space = " " * multiplier
        saved_space = " " * 5
        print(f"{space}{saved_space}    _________________   ")
        print(f"{space}{saved_space}    |   GAME OVER   |   ")
        print(f"{space}{saved_space}    |_______________|   ")
        print()
        print(f"{space}{saved_space}     _ ._  _ , _ ._     ")
        print(f"{space}{saved_space}   (_ ' ( `  )_  .__)   ")
        print(f"{space}{saved_space} ( (  (    )   `)  ) _) ")
        print(f"{space}{saved_space}(__ (_   (_ . _) _) ,__)")
        print(f"{space}{saved_space}    `~~`\\ ' . /`~~`     ")
        print(f"{space}{saved_space}         ;   ;          ")
        print(f"{space}{saved_space}         /   \\          ")
        print(f"{space}{saved_space}        /     \\         ")

def print_images():
    if percent < 10:
        print_kaboom()
        print_car()
        print_below_spaces()
        print_ground()
    else:
        print_winner()

def main_menu():
    pass

# =========================================================================================================

def update():
    global isGameOver

    while not isGameOver and not isGameWinner:
        os.system("cls")
        print_images()
        gameplay_loop()

def last_update():
    os.system("cls")
    print_images()

    print()
    print(f"{'=======================':^50}")
    print(f"{endGameWords[languageSelected]['End']:^50}")
    print(f"{'=======================':^50}")
    print()
    print(f" {endGameWords[languageSelected]['Movie']} >> {randomWord.replace('+', ' ')}")
    print()
    print(f" {endGameWords[languageSelected]['Attempt']} >> ", end="")
    for l in wordToComplete:
        print(l, end="")
    print()
    print(f" {endGameWords[languageSelected]['Percent']} >> {(int(percent))*10}%  ({(len(randomWord)) - wordsToDiscover - randomWord.count('+')}/{len(randomWord) - randomWord.count('+')})")
    print(f" {endGameWords[languageSelected]['Tries']} >> {len(letterHistory)} : ", end='')
    for l in letterHistory:
        print(l, end="")
    print()
    print()
    print(f"{'>> ENTER TO CONTINUE << ':^50}")
    input('')
    for i in range(3, -1, -1):
        print(f" {'>'*(i+1)} {i}")
        sleep(1)

def final_animation():
    if isGameWinner:
        Frames.play_win_final_anim()
    elif isGameOver:
        Frames.play_death_final_anim()



# GAME LOOP ==============================================================================================

start()
update()
last_update()
final_animation()