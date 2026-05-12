import random

def computer_choose_rand_word():
    words = [
    "apple", "beach", "cloud", "drink", "ghost", "house", "lemon", "music", 
    "pizza", "smile", "tiger", "water", "balloon", "camera", "dancing", 
    "explore", "friends", "guitar", "journey", "kitchen", "mystery", 
    "orange", "puzzle", "rocket", "sunlight", "whisper", "adventure", 
    "astronaut", "championship", "diamond", "elevator", "flamingo", 
    "hospital", "labyrinth", "mountain", "nightmare", "orchestra", 
    "satellite", "umbrella", "volcano", "jazz", "rhythm", "oxygen", 
    "queue", "sphinx", "whizz", "zigzag", "awkward"
    ]
    return list(random.choice(words))


def encrypt_word(comp_choice : list):
    return ["X" for w in comp_choice]


def user_input_letter():
    while True:
        user_letter = input("Enter a letter: ").lower()
        if len(user_letter) > 1:
            print("You can enter only one char.")
            continue
        if not user_letter.isalpha():
            print("You can enter only a letter.")
            continue
        return user_letter

# def check_letter_in_word(user_letter : str, comp_choice : list):