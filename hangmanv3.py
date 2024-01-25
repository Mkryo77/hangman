import random
from words import word_list
from animals import animals_list
from english_cities import english_cities_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def get_animal():
    animal = random.choice(animals_list)
    return animal.upper()

def get_english_city():
    english_city = random.choice(english_cities_list)
    return english_city.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 9
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well done,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Well done! You guessed the word! You Win!")
    else:
        print("You ran out of tries you idiot. The word was " + word + ". Maybe next time!")
    
def play(animal):
    animal_completion = "_" * len(animal)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 9
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(animal_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in animal:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well done,", guess, "is in the word!")
                guessed_letters.append(guess)
                animal_as_list = list(animal_completion)
                indices = [i for i, letter in enumerate(animal) if letter == guess]
                for index in indices:
                    animal_as_list[index] = guess
                animal_completion = "".join(animal_as_list)
                if "_" not in animal_completion:
                    guessed = True
        elif len(guess) == len(animal) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != animal:
                print(guess, "is not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                animal_completion = animal
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(animal_completion)
        print("\n")
    if guessed:
        print("Well done! You guessed the word! You Win!")
    else:
        print("You ran out of tries you idiot. The word was " + animal + ". Maybe next time!")    

def play(english_city):
    english_city_completion = "_" * len(english_city)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 9
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(english_city_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in english_city:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well done,", guess, "is in the word!")
                guessed_letters.append(guess)
                english_city_as_list = list(english_city_completion)
                indices = [i for i, letter in enumerate(english_city) if letter == guess]
                for index in indices:
                    english_city_as_list[index] = guess
                english_city_completion = "".join(english_city_as_list)
                if "_" not in english_city_completion:
                    guessed = True
        elif len(guess) == len(english_city) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != english_city:
                print(guess, "is not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                english_city_completion = english_city
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(english_city_completion)
        print("\n")
    if guessed:
        print("Well done! You guessed the word! You Win!")
    else:
        print("You ran out of tries you idiot. The word was " + english_city + ". Maybe next time!")  

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
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
                """,
                # just frame
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # frame no top
                """
                   
                   |     
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # initial
                """
                   
                         
                         
                       
                         
                        
                   
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    animal = get_animal()
    english_city = get_english_city()
    category = input("Please choose a category. 'Words', 'Animals' or 'English Cities'? ").upper()
    if category == "WORDS":
        word = get_word()
        play(word)
    elif category == "ANIMALS":
        animal = get_animal()
        play(animal)
    elif category == "ENGLISH CITIES":
        english_city = get_english_city()
        play(english_city)
    else:
        print("Not a valid category.")
        main()
    while input("Would you like to play again? (Y/N) ").upper() == "Y":
        main()
    else:
        print("Thanks for playing!")
        exit()

if __name__ == "__main__":
    main()