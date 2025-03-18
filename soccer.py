import random

def get_player_data():
    return {
        "Lionel Messi": {"clubs": ["Barcelona", "Paris Saint-Germain", "Inter Miami"], "goals": 821, "assists": 350, "appearances": 1030},
        "Cristiano Ronaldo": {"clubs": ["Sporting CP", "Manchester United", "Real Madrid", "Juventus", "Al Nassr"], "goals": 875, "assists": 250, "appearances": 1150},
        "Neymar": {"clubs": ["Santos", "Barcelona", "Paris Saint-Germain", "Al Hilal"], "goals": 430, "assists": 230, "appearances": 700},
        "Zlatan Ibrahimovic": {"clubs": ["Malmo FF", "Ajax", "Juventus", "Inter Milan", "Barcelona", "AC Milan", "Paris Saint-Germain", "Manchester United", "LA Galaxy"], "goals": 570, "assists": 250, "appearances": 900},
        "David Beckham": {"clubs": ["Manchester United", "Real Madrid", "LA Galaxy", "AC Milan", "Paris Saint-Germain"], "goals": 127, "assists": 180, "appearances": 834},
        "Ronaldinho": {"clubs": ["Gremio", "Paris Saint-Germain", "Barcelona", "AC Milan", "Flamengo", "Atletico Mineiro"], "goals": 300, "assists": 200, "appearances": 750},
        "Kaka": {"clubs": ["Sao Paulo", "AC Milan", "Real Madrid", "Orlando City"], "goals": 237, "assists": 150, "appearances": 700},
        "Thierry Henry": {"clubs": ["Monaco", "Juventus", "Arsenal", "Barcelona", "New York Red Bulls"], "goals": 411, "assists": 200, "appearances": 920},
        "Wayne Rooney": {"clubs": ["Everton", "Manchester United", "DC United", "Derby County"], "goals": 366, "assists": 250, "appearances": 883},
        "Xavi": {"clubs": ["Barcelona", "Al Sadd"], "goals": 93, "assists": 210, "appearances": 900}
    }

def play_game():
    players = get_player_data()
    score = 0
    rounds = 3
    
    print("Welcome to 'Guess the Soccer Career'! Try to guess the footballers based on their career stats.")
    
    for _ in range(rounds):
        player_name = random.choice(list(players.keys()))
        data = players[player_name]
        
        print("\nClubs:")
        for club in data["clubs"]:
            print(f"- {club}")
        
        print(f"Total Goals: {data['goals']}")
        print(f"Total Assists: {data['assists']}")
        print(f"Total Appearances: {data['appearances']}")
        
        guess = input("Who is this player? ").strip()
        
        if guess.lower() == player_name.lower():
            print("Correct! You guessed it right.")
            score += 1
        else:
            print(f"Wrong! The correct answer was {player_name}.")
    
    print(f"\nGame over! Your final score: {score}/{rounds}")

if __name__ == "__main__":
    play_game()
