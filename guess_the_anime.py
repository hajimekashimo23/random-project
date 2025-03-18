import random

anime_data = {
    "A boy discovers he has incredible powers and embarks on a journey to become the strongest hero.": "My Hero Academia",
    "A young ninja dreams of becoming the leader of his village while facing many powerful enemies.": "Naruto",
    "A group of pirates sail the seas in search of the ultimate treasure.": "One Piece",
    "A boy is transported to a fantasy world where he gains the ability to return from death.": "Re:Zero",
    "Teenagers pilot massive humanoid robots to fight mysterious creatures called Angels.": "Neon Genesis Evangelion",
    "A high school student discovers a notebook that allows him to kill anyone by writing their name in it.": "Death Note",
    "A group of students must survive in a high school controlled by a sadistic bear.": "Danganronpa",
    "A world where people are born with unique abilities called quirks and heroes battle villains.": "My Hero Academia",
    "A family of assassins and spies must pretend to be normal while hiding their secrets.": "Spy x Family",
    "A young girl falls into another world filled with spirits and must find a way home.": "Spirited Away"
}

def get_hint():
    hint, title = random.choice(list(anime_data.items()))
    return hint, title

def play_game():
    hint, title = get_hint()
    print("Guess the anime title based on the hint:")
    print(hint)
    
    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").strip()
        if guess.lower() == title.lower():
            print("Correct! You guessed the anime title.")
            break
        else:
            attempts -= 1
            print(f"Incorrect. You have {attempts} attempts left.")
    
    if attempts == 0:
        print(f"Game over! The correct answer was: {title}")
    
    retry = input("Would you like to play again? (yes/no): ").strip().lower()
    if retry == "yes":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
