import random

MAX_ROUNDS = 5

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


def user_input_letter(user_letters : list):
    while True:
        user_letter = input("Enter a letter: ").lower()
        if len(user_letter) > 1:
            print("You can enter only one char.")
            continue
        if not user_letter.isalpha():
            print("You can enter only a letter.")
            continue
        if user_letter in user_letters:
            print("You have already chosen this letter.")
            continue
        return user_letter


def check_letter_in_word(user_letter : str, comp_choice : list):
    if user_letter in comp_choice:
        return True
    return False


def insert_letter_to_word(user_letter : str, comp_choice : list, enc_word : list):
    for i,l in enumerate(comp_choice):
        if user_letter == l:
            enc_word[i] = user_letter
    return enc_word


def check_if_completed_word(enc_word : list):
    if "X" not in enc_word:
        return True
    return False


def main():
    print("=== HangMan ===")
    comp_choice = computer_choose_rand_word()
    enc_word = encrypt_word(comp_choice)
    rounds_counter = 0
    user_letters = []
    while rounds_counter < MAX_ROUNDS:
        print(MAX_ROUNDS - rounds_counter, "Rounds left")
        print("".join(enc_word))
        print("Letter that you gusset", user_letters)
        user_letter = user_input_letter(user_letters)
        user_letters.append(user_letter)
        if check_letter_in_word(user_letter, comp_choice):
            enc_word = insert_letter_to_word(user_letter, comp_choice, enc_word)
            print("The letter in the word.")
        else:
            rounds_counter += 1
            print("The letter does not exist in the word, Try again")
            continue
        if check_if_completed_word(enc_word):
            print(f"You Won. \nThe word is **{"".join(enc_word)}**")
            return
        
    print(f"No more rounds. Game over... \nThe word was **{"".join(comp_choice)}**")


if __name__ == "__main__":       
    main()