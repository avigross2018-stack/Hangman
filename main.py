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
    return random.choice(words).split()

print(computer_choose_rand_word())