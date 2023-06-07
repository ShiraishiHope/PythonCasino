#! usr/bin/env python3

import sys

class Score:
    def __init__(self):
        self.filename = 'score.txt'

    def check_user(self, user):
        found_user = False
        with open(self.filename, 'r+') as score:
            for line in score:
                parts = line.strip().split(';')
                if user.name == parts[0]:
                    if int(parts[1]) == 0:
                        self.buy_in(user)
                        found_user = True
                    else:
                        funds = int(parts[1])
                        user.user_funds(funds)
                        found_user = True
                        break

            if not found_user:
                user.funds = 100
                score.write(f"{user.name};100\n")
            
    def reorganize_scores(self):
        # Read the lines from the text document
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        # Extract the name and score
        extracted_parts = []
        for line in lines:
            parts = line.strip().split(';')
            if len(parts) >= 2:
                name = parts[0]
                try:
                    score = int(parts[1])  # Assuming the score is an integer
                    extracted_parts.append((name, score))
                except ValueError:
                    print(f"Invalid score format in line: {line}")
            else:
                print(f"Invalid line format: {line}")

        # Sort the list of extracted parts in descending order based on the score
        sorted_parts = sorted(extracted_parts, key=lambda x: x[1], reverse=True)

        # Print or write the reorganized lines
        print("\nScores:\n")
        for part in sorted_parts:
            name, score = part
            print(name, score)
    
    def buy_in(self, user):
        while True:
            choice = input("You have zero funds. Do you want to buy in? (Y/N): ")
            if choice.upper() == 'Y':
                amount = input("Enter the amount to add (up to 50): ")
                try:
                    amount = int(amount)
                    if 0 < amount <= 50:
                        user.user_funds(amount)
                        self.update_score(user, amount)
                        print(f"Funds added: {amount}")
                        break
                    else:
                        print("Invalid amount. Please enter a value between 1 and 50.")
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            elif choice.upper() == 'N':
                print("Thanks for your patronage, we hope to see you again soon.")
                sys.exit()
            else:
                print("Invalid choice. Please enter Y or N.")   

    def update_score(self, user, profit):
        with open(self.filename, 'r+') as score:
            lines = score.readlines()
            score.seek(0)
        
            for i, line in enumerate(lines):
                parts = line.strip().split(';')
                if user.name == parts[0]:
                    current_score = int(parts[1])
                    new_score = current_score + profit
                    lines[i] = f"{user.name};{new_score}\n"
                    break
        
            score.seek(0)
            score.writelines(lines)
            score.truncate()