"""
PROJECT 1: SNAKE, WATER, GUN GAME

This is a classic hand game similar to Rock-Paper-Scissors.
Rules:
  - Snake drinks Water -> Snake wins
  - Water erodes Gun   -> Water wins
  - Gun kills Snake    -> Gun wins

If both choose the same, it's a tie.

Concepts used:
  - Variables & Data Types (strings, integers)
  - Operators (comparison, logical)
  - Conditional statements (if-elif-else)
  - Loops (while for replay)
  - Functions (modular code)
  - User input & random module
"""

import random

def get_computer_choice():
    """Randomly select and return computer's move."""
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on game rules.
    Returns:
        "user" if user wins,
        "computer" if computer wins,
        "tie" if it's a tie.
    """
    # Tie condition
    if user_choice == computer_choice:
        return "tie"

    # Winning rules for user
    # user: snake beats water
    if user_choice == "snake" and computer_choice == "water":
        return "user"
    # user: water beats gun
    elif user_choice == "water" and computer_choice == "gun":
        return "user"
    # user: gun beats snake
    elif user_choice == "gun" and computer_choice == "snake":
        return "user"
    # All other cases => computer wins
    else:
        return "computer"

def display_choices(user_choice, computer_choice):
    """Prints both players' choices."""
    print(f"\nYou chose: {user_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")

def display_result(winner, user_score, computer_score):
    """Announces winner and shows current scores."""
    if winner == "user":
        print("🎉 You win this round!")
    elif winner == "computer":
        print("💻 Computer wins this round!")
    else:
        print("🤝 It's a tie!")
    
    print(f"Score -> You: {user_score}  Computer: {computer_score}")

def get_user_choice():
    """
    Asks user for input, validates, returns lowercase full word.
    Accepts: snake, water, gun or s, w, g.
    """
    while True:
        choice = input("\nEnter your move (snake/water/gun or s/w/g): ").strip().lower()
        
        # Map shortcuts to full words
        if choice in ["snake", "s"]:
            return "snake"
        elif choice in ["water", "w"]:
            return "water"
        elif choice in ["gun", "g"]:
            return "gun"
        else:
            print("Invalid input! Please enter snake, water, gun or s, w, g.")

def play_again():
    """Ask user if they want to play again. Returns True if yes."""
    answer = input("\nDo you want to play another round? (yes/no or y/n): ").strip().lower()
    return answer in ["yes", "y"]

def main():
    """Main game loop."""
    print("=" * 40)
    print("    SNAKE - WATER - GUN GAME")
    print("=" * 40)
    print("Rules:")
    print("  Snake drinks Water  -> Snake wins")
    print("  Water erodes Gun    -> Water wins")
    print("  Gun kills Snake     -> Gun wins")
    print("=" * 40)

    user_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        rounds_played += 1
        print(f"\n--- ROUND {rounds_played} ---")
        
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Show both choices
        display_choices(user_choice, computer_choice)
        
        # Determine winner
        winner = determine_winner(user_choice, computer_choice)
        
        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        # Display result
        display_result(winner, user_score, computer_score)
        
        # Ask for replay
        if not play_again():
            print("\nThanks for playing! Final score:")
            print(f"You: {user_score}  Computer: {computer_score}")
            if user_score > computer_score:
                print("🏆 You are the overall winner!")
            elif computer_score > user_score:
                print("💻 Computer is the overall winner!")
            else:
                print("🤝 Overall it's a tie!")
            break

if __name__ == "__main__":
    main()