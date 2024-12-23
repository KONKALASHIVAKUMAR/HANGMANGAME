import random

def hangman():
    # List of words to choose from
    word_list = ['python', 'programming', 'hangman', 'challenge', 'developer']
    secret_word = random.choice(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    # Display initial game status
    print("Welcome to Hangman!")
    print("_ " * len(secret_word))
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            incorrect_guesses += 1
        
        # Display current state of the word
        current_state = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print(" ".join(current_state))
        
        # Check if the player has guessed the entire word
        if '_' not in current_state:
            print("Congratulations! You've guessed the word correctly!")
            break
        
        # Display remaining attempts
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
    
    else:
        print(f"Game over! The word was '{secret_word}'. Better luck next time!")

# Run the game
hangman()
