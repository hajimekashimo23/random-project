import time
import random

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def haunted_house():
    slow_print("You wake up in a dark, abandoned house. The air is cold, and you hear whispers around you...")
    
    choice1 = input("Do you want to explore the house? (Yes/No): ").strip().lower()
    
    if choice1 == "yes":
        slow_print("You step forward, the wooden floor creaking under your weight. You see two doors ahead.")
        choice2 = input("Do you enter the LEFT door or the RIGHT door? (Left/Right): ").strip().lower()
        
        if choice2 == "left":
            slow_print("You find yourself in an old library. Suddenly, a book falls off the shelf by itself...")
            choice3 = input("Do you pick up the book? (Yes/No): ").strip().lower()
            
            if choice3 == "yes":
                slow_print("As soon as you open the book, shadowy hands pull you inside! GAME OVER.")
            else:
                slow_print("You ignore the book and leave the library safely. You survive... for now.")
                slow_print("You enter another hallway with flickering lights. A whisper calls your name.")
                choice4 = input("Do you follow the whisper? (Yes/No): ").strip().lower()
                
                if choice4 == "yes":
                    slow_print("The whisper leads you to a dusty bedroom. There's an old diary on the table.")
                    choice5 = input("Do you read the diary? (Yes/No): ").strip().lower()
                    
                    if choice5 == "yes":
                        slow_print("The diary tells a tragic story of a family that vanished. The last page says: 'You are next.'")
                        slow_print("A shadow figure appears behind you. RUN!")
                    else:
                        slow_print("You leave the room quickly and find another staircase leading to the attic.")
                        choice6 = input("Do you go up to the attic? (Yes/No): ").strip().lower()
                        
                        if choice6 == "yes":
                            slow_print("The attic is filled with old toys. One of them starts moving on its own...")
                            choice7 = input("Do you pick up the toy? (Yes/No): ").strip().lower()
                            
                            if choice7 == "yes":
                                slow_print("The toy whispers: 'Play with me... forever.' Your vision fades. GAME OVER.")
                            else:
                                slow_print("You resist the temptation and find a hidden trapdoor leading outside. YOU SURVIVE!")
                        else:
                            slow_print("You decide not to go up. The door behind you slams shut. GAME OVER.")
                else:
                    slow_print("You ignore the whisper and keep walking. The exit is near! YOU SURVIVE!")
        
        elif choice2 == "right":
            slow_print("You enter a candle-lit room with a mirror. Your reflection doesn't move...")
            choice3 = input("Do you touch the mirror? (Yes/No): ").strip().lower()
            
            if choice3 == "yes":
                slow_print("Your reflection smiles wickedly and pulls you inside. You are trapped forever! GAME OVER.")
            else:
                slow_print("You step back just in time. The reflection disappears. YOU SURVIVE!")
                slow_print("You find another hallway with flickering lights. The walls are covered in strange symbols.")
                choice4 = input("Do you try to decipher the symbols? (Yes/No): ").strip().lower()
                
                if choice4 == "yes":
                    slow_print("The symbols tell a story of an ancient curse. A shadowy figure approaches!")
                    choice5 = input("Do you run or fight? (Run/Fight): ").strip().lower()
                    
                    if choice5 == "run":
                        slow_print("You sprint down the hallway and find a hidden passage leading outside. YOU SURVIVE!")
                    else:
                        slow_print("You grab a nearby candlestick and swing at the figure. It vanishes! But the house begins to collapse... RUN!")
                else:
                    slow_print("You ignore the symbols and keep moving. The house trembles as you step forward...")
                    choice6 = input("Do you hide or keep going? (Hide/Go): ").strip().lower()
                    
                    if choice6 == "hide":
                        slow_print("You hide in a closet, but something is already inside... GAME OVER.")
                    else:
                        slow_print("You push forward and find the main door unlocked. YOU ESCAPE! YOU WIN!")
        
        else:
            slow_print("You hesitate for too long. The darkness consumes you... GAME OVER.")
    
    elif choice1 == "no":
        slow_print("You stay still, but the shadows creep closer... GAME OVER.")
    
    else:
        slow_print("Indecision is deadly in this place... GAME OVER.")

haunted_house()
