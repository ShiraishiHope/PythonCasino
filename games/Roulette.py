from games.Game import Game
import random
import math

class Roulette(Game):
    def __init__(self, score):
        super().__init__("Roulette")
        self.score = score
    
    def run(self, user):
        while user.funds > 0:
            print("1. Play")
            print("q. Quit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.play(user)
            elif choice.lower() == "q":
                print("Returning to the previous menu...")
                break
            else:
                print("Invalid input. Please try again.")
    
    def play(self, user):
        funds = user.funds
        while True:
            amount = input(f"Enter the amount to play (up to {funds}): ")
            try:
                amount = int(amount)
                if 0 < amount <= funds:
                    break
                else:
                    print("Invalid amount. Please enter a value between 1 and your available funds.")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

        # Deduct the bet amount from user's funds
        self.score.update_score(user, -amount)
        user.update_funds(-amount)

        user_number = self.get_user_number()

        # Generate a random number between 0 and 49 (inclusive)
        winning_number = random.randint(0, 49)
        
        print(f"Winning number: {winning_number}")
        
        if winning_number == user_number:
            print(f"Congratulations! You guessed the exact number! You won {amount * 3}€!")
            self.score.update_score(user, amount * 3)
            user.update_funds(amount*3) 
        elif user_number % 2 == winning_number % 2:
            winnings = math.ceil(amount * 0.5)  # 50% of the original bet rounded down
            print(f"Congratulations! The numbers are of the same type (even or odd). You won {winnings}€!")
            self.score.update_score(user, winnings)
            user.update_funds(winnings) 
        else:
            print("Sorry, you didn't win this time.")

    def get_user_number(self):
        while True:
            number = input("Choose a number between 0 and 49: ")
            try:
                number = int(number)
                if 0 <= number <= 49:
                    return number
                else:
                    print("Invalid number. Please enter a value between 0 and 49.")
            except ValueError:
                print("Invalid number. Please enter a valid integer.")

