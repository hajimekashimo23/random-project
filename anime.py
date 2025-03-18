import random

# List of anime characters with hints
characters = [
    {"name": "Goku", "hints": ["I am a Saiyan", "I love to fight", "My signature move is Kamehameha"]},
    {"name": "Luffy", "hints": ["I am a pirate", "I want to be the Pirate King", "I have a stretchy body"]},
    {"name": "Naruto", "hints": ["I am a ninja", "I have a fox spirit inside me", "My dream is to be Hokage"]},
    {"name": "Light Yagami", "hints": ["I found a mysterious notebook", "I want to be the god of a new world", "I am very intelligent"]},
    {"name": "Levi Ackerman", "hints": ["I am humanity’s strongest soldier", "I fight Titans", "I am from the Survey Corps"]},
    {"name": "Gojo Satoru", "hints": ["I am a teacher", "I have powerful eyes", "I use Limitless and Infinity"]},
]

def play_game():
    print("Welcome to Guess the Anime Character!")
    score = 0
    
    # Shuffle characters for randomness
    random.shuffle(characters)
    
    for character in characters:
        print("\nGuess the character!")
        random.shuffle(character['hints'])  # Randomize hint order
        
        for i, hint in enumerate(character['hints'], start=1):
            print(f"Hint {i}: {hint}")
            guess = input("Your guess: ").strip()
            
            if guess.lower() == character['name'].lower():
                print("Correct! You got it!")
                score += 10  # Add points for a correct guess
                break
            else:
                print("Wrong! Try again.")
                
            if i == len(character['hints']):
                print(f"Out of hints! The correct answer was {character['name']}")
    
    print(f"\nGame over! Your final score is {score}")

if __name__ == "__main__":
    play_game()
