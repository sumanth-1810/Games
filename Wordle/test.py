from rich.prompt import Prompt #importing rich
from rich.console import Console
from random import choice #importing random to choose a word from word_list in words.py
from words import word_list

SQUARES = {
    'correct_place': '🟩', #colour for correct position and letter
    'correct_letter': '🟨', #colour for incorrect position but correct letter
    'incorrect_letter': '⬛' #colour for incorrext position and letter
}

WELCOME_MESSAGE = f'\n[white on magenta] WELCOME TO WORDLE [/]\n' #using rich to get lively interface
PLAYER_INSTRUCTIONS = f'\n[white on blue] You may start guessing [/]\n' #instructions to play game
GUESS_STATEMENT = f'\n[white on magenta] Enter your guess [/]\n' 
ALLOWED_GUESSES = 6 #number of guesses allowed 

def correct_place(letter): #function for letter in correct place
    return f'[black on green\n]{letter}[/]' #colour code


def correct_letter(letter): #function for correct letter  
    return f'[black on yellow\n]{letter}[/]' #colour code


def incorrect_letter(letter): #function for wrong letter
    return f'[white on black\n]{letter}[/]' #colour code


#function to check if guessed word is correct or not:

def check_guess(guess, answer): 
    guessed = [] #store guessed word
    wordle_pattern = [] #store correct word
    for i, letter in enumerate(guess): #for loop to check the word letter by letter
        if answer[i] == guess[i]: #if strings match...
            guessed += correct_place(letter) #call correct_place function (colour green)
            wordle_pattern.append(SQUARES['correct_place']) #final output, add green block
        elif letter in answer: #if the letter is correct, but is in the wrong place...
            guessed += correct_letter(letter) #call correct_letter function
            wordle_pattern.append(SQUARES['correct_letter']) #final output, add yellow block
        else: #if not the above 2 conditions, the letter is not in the word
            guessed += incorrect_letter(letter) #hence, call incorrect_letter function
            wordle_pattern.append(SQUARES['incorrect_letter']) #final output, add black block
    return ''.join(guessed), ''.join(wordle_pattern)


#game loop:

def game(console, chosen_word): 
    end_of_game = False #boolean type variable responsible for running of the while loop
    already_guessed = [] #stores the word that has already been guessed
    full_wordle_pattern = [] #contains wordle pattern (correct word)
    all_words_guessed = [] #contains words with the colours

    while not end_of_game: 
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        while len(guess) != 5 or guess in already_guessed: #check if guessed word has 5 letters or has already been gueseed
            if guess in already_guessed:
                console.print("[red]You've already guessed this word!!\n[/]") #print if already guessed
            else:
                console.print('[red]Please enter a 5-letter word!!\n[/]') #print if the word length isn't 5
            guess = Prompt.ask(GUESS_STATEMENT).upper() #call the functions for respective turn
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word) #check the entered word
        all_words_guessed.append(guessed) #storing
        full_wordle_pattern.append(pattern) #storing

        console.print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES: #if guessed word attributes are same as that of chosen word...
            end_of_game = True #terminate loop
    if len(already_guessed) == ALLOWED_GUESSES and guess != chosen_word: #if guess is wrong...
        console.print(f"\n[red]WORDLE X/{ALLOWED_GUESSES}[/]") #print massage
        console.print(f'\n[green]Correct Word: {chosen_word}[/]') 
    else: #end game
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n") #print at the end, after completion
    console.print(*full_wordle_pattern, sep="\n")


#main function:

if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
    game(console, chosen_word)