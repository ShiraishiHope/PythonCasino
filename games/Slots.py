from games.Game import Game
import random

class Slots(Game):
    def __init__(self, score):
        super().__init__("Slots")
        self.score = score
    
    def run(self, user):
        while user.funds > 0:                
            print
            print("1. Play 1€")
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
        
        
        # Deduct the 1€ bet
        self.score.update_score(user, -1)
        user.update_funds(-1)  
        
        # Generate three random numbers between 1 and 7
        numbers = [random.randint(1, 7) for _ in range(3)]
        
        print(f"Numbers: {numbers}")
        
        if numbers == [7, 7, 7]:
            print("Congratulations! You won 500€!")
            self.score.update_score(user, 500)
            user.update_funds(500) 
        elif len(set(numbers)) == 1:
            print("Congratulations! You won 10€!")
            self.score.update_score(user, 10)
            user.update_funds(10) 
        elif list(range(min(numbers), max(numbers)+1)) == sorted(numbers):
            print("Congratulations! You won 5€!")
            self.score.update_score(user, 5)
            user.update_funds(5) 
        else:
            print("Sorry, you didn't win this time.")
