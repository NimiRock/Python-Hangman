import os

##### Functions:
def check_file_validity(path):
    """
    This function checks the validity of the file path
    :param path: The path of the file
    :type file_path: string
    :return: The same path if correct, or if path broken - a corrected path
    :rtype: string
    """
    while not (os.path.isfile(path)):
        path = input("The file does not exist, or the path is broken, please try again: ")
    return path

def choose_word(file_path, index):
    """
    This function get the secret word from the document according to the user's chosen index.
    :param file_path: The full path of the file, including read() function
    :param index: The index of the desired word (the user can only choose from 1 and up, and the function cconvert accordingly)
    :type file_path: string
    :type index: integer
    :return: The secret game word
    :rtype: string
    """
    list_of_words = file_path.split()
    filtered_list = []
    for word in list_of_words:
        if (word in filtered_list):
            continue
        else:
            filtered_list.append(word)
    if (len(list_of_words) <= index):
        index -= len(list_of_words)
    return list_of_words[index - 1].lower()


def check_win(game_word, old_letters_guessed):
    """
    This function gets the secret word, and the old letters that the user guessed, and checks if he won or not.
    :param game_word: The secret word
    :param old_letters_guessed: A list containing all of the words that the user guessed
    :type file_path: string
    :type index: list
    :return: "True" if all the letters in the secret word are in the old letters list, "False" if a letter is not in the old letters
    :rtype: boolean
    """
    for letter in game_word:
        if (letter in old_letters_guessed):
            continue
        else:
            return False
    return True


def show_hidden_word(game_word, old_letters_guessed):
    """
    This function show the words in old letters guessed list, if they are also in the secret word, or "_" instead
    :param game_word: The secret word
    :param old_letters_guessed: A list containing all of the words that the user guessed
    :type game_word: string
    :type old_letters_guessed: list
    :return: current situation containing correct words and "_" for undiscovered words
    :rtype: string
    """
    i = 0
    current_situation = ""
    for letter in game_word:
        if letter in old_letters_guessed:
            current_situation += letter + " "
            i += 1
        else:
            current_situation += "_ "
            i += 1


    return current_situation


def check_valid_input(user_guess, old_letters_guessed):
    """
    This function checks if you already guessed the word, and require you to change your guess if needed
    :param user_guess: The letter the user guessed
    :param old_letters_guessed: A list containing all of the words that the user guessed
    :type user_guess: string
    :type old_letters_guessed: list
    :return: The same letter if input is valid, or corrected input if the initial was invalid
    :rtype: string
    """
    while (user_guess in old_letters_guessed):
        print("\nYou already guessed that letter")
        print("Previous Guesses: " + " -> ".join(old_letters_guessed))
        user_guess = input("Please select another letter: ")
    return user_guess


def try_update_letter_guessed(user_guess, old_letters_guessed):
    """
    This function checks if you already guessed the word, or if your input is invalid (number, symbol, etc..) and require you to change your guess if needed
    :param user_guess: The letter the user guessed
    :param old_letters_guessed: A list containing all of the words that the user guessed
    :type user_guess: string
    :type old_letters_guessed: list
    :return: The same letter if input is valid, or corrected input if the initial was invalid
    :rtype: string
    """
    while ((user_guess in old_letters_guessed) or (len(user_guess) != 1) or (not user_guess.isalpha())):
        print("\nYour input is invalid or you already guessed that letter")
        print("Previous Guesses: " + " -> ".join(old_letters_guessed))
        user_guess = input("Please select another letter: ")
    return user_guess

def print_hangman(num_of_tries):
    return HANGMAN_PHOTOS[num_of_tries]




def play_game(file_path):
    """
    This is the main game function. It calls all of the other functions, and display the opening screen.
    :param file_path: The full path of the file, including read() function
    :type file_path: string
    :return: "WIN" if the player won, "LOSE" if the player lost
    :rtype: string
    """
    os.system('cls')
    input("""
 _    _
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                    |___/
Number of tries: 7

Press enter to start""")
    
    index = input("Please choose a number from 1 and up, then press enter: ")
    while ((len(index) < 0) or (not index.isnumeric())):
        index = input("Invalid number, try again: ")
    index = int(index)
    game_word = choose_word(file_path, index)
    old_letters_guessed = []
    current_situation = ["_ "] * len(game_word)
    bad_tries = 0
    while ((bad_tries < 7) and ("_ " in current_situation)):
        print(''.join(current_situation) + "\n")
        user_guess = input("Insert a letter, then press enter: ").lower()
        user_guess = check_valid_input(user_guess, old_letters_guessed).lower()
        user_guess = try_update_letter_guessed(user_guess, old_letters_guessed).lower()
        old_letters_guessed.append(user_guess)
        if user_guess in game_word:
            print("\nGuessed it right!" + "\n\n")
        current_situation = show_hidden_word(game_word, old_letters_guessed)
        if not (user_guess in game_word):
            print(f"\nThe letter {user_guess} is not in the word!")
            bad_tries += 1
        print(print_hangman(bad_tries))
        if (check_win(game_word, old_letters_guessed)):
            return "WIN!"
        elif(bad_tries == 7):
            return f"""
LOSE!
The word was: {game_word}
"""


##### Variables
HANGMAN_PHOTOS = {
    0: "",
    1: """
    x-------x
    """,
    2: """
    x-------x
    |
    |
    |
    |
    |
    """,
    3: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""}

path = check_file_validity(input("Please enter the full path of a file containing words in the following format (word word word): "))
file_path = open(path, "r").read()

##### main() function
def main():
    print(play_game(file_path))
    while (input("Play again? Y / N: ").lower() == "y"):
        open(path, "r").close()
        os.system('cls')
        play_game(file_path)


if __name__ == "__main__":
    main()
