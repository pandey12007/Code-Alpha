import random
import pandas

# List of possible words
words = ["python", "hangman", "challenge", "programming", "openai","Kashyap","abhishek","abilities"]

# Function to select a random word from the list
def select_word():
    return random.choice(words)

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '?'
    return display

# Function to play the Hangman game
def play_hangman():
    word = select_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            print(f"Good guess! {guess} is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, {guess} is not in the word.")
            guessed_letters.add(guess)
            incorrect_guesses += 1
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was: {word}")


play_hangman()
