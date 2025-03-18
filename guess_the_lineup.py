import random

data = {
    "2014 FIFA World Cup Final": {
        "team": "Germany",
        "players": ["Neuer", "Lahm", "Hummels", "Boateng", "Howedes", "Schweinsteiger", "Kramer", "Kroos", "Ozil", "Muller", "Klose"]
    },
    "2005 Champions League Final": {
        "team": "Liverpool",
        "players": ["Dudek", "Finnan", "Carragher", "Hyypia", "Traore", "Xabi Alonso", "Gerrard", "Riise", "Kewell", "Luis Garcia", "Baros"]
    },
    "2022 FIFA World Cup Final": {
        "team": "Argentina",
        "players": ["Emiliano Martinez", "Molina", "Romero", "Otamendi", "Tagliafico", "De Paul", "Fernandez", "Mac Allister", "Messi", "Di Maria", "Alvarez"]
    },
    "2010 FIFA World Cup Final": {
        "team": "Spain",
        "players": ["Casillas", "Ramos", "Puyol", "Pique", "Capdevila", "Busquets", "Xabi Alonso", "Xavi", "Iniesta", "Pedro", "Villa"]
    },
    "2008 Champions League Final": {
        "team": "Manchester United",
        "players": ["Van der Sar", "Brown", "Ferdinand", "Vidic", "Evra", "Hargreaves", "Scholes", "Carrick", "Cristiano Ronaldo", "Rooney", "Tevez"]
    }
}

def get_match():
    match = random.choice(list(data.keys()))
    return match, data[match]

def play_game():
    match, details = get_match()
    print(f"Guess the starting lineup of {details['team']} in the {match}!")
    guessed = set()
    attempts = 0
    max_attempts = len(details['players']) + 5
    correct = 0
    
    while correct < len(details['players']) and attempts < max_attempts:
        guess = input("Enter a player's name (or type 'hint' for help): ").strip()
        attempts += 1
        
        if guess.lower() == 'hint':
            remaining = [p for p in details['players'] if p not in guessed]
            if remaining:
                print(f"Hint: One of the remaining players is {random.choice(remaining)}")
            else:
                print("No more hints available!")
            continue
        
        if guess in details['players'] and guess not in guessed:
            guessed.add(guess)
            correct += 1
            print(f"Correct! {correct}/{len(details['players'])} guessed.")
        else:
            print("Incorrect or already guessed.")
    
    if correct == len(details['players']):
        print(f"Congratulations! You guessed the full lineup of {details['team']}.")
    else:
        print(f"Game over! The full lineup was: {', '.join(details['players'])}")
    
    retry = input("Would you like to play again? (yes/no): ").strip().lower()
    if retry == "yes":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
