from User import User
from Score import Score
from games.Slots import Slots
from games.Roulette import Roulette
import getpass

score = Score()

name = input("name: ")
password = getpass.getpass("password: ")

user1 = User(name)
user1.set_password(password)

score.check_user(user1)
score.reorganize_scores()

while True:
    print(f"Your funds: {user1.funds}")
    if user1.funds <= 0:
        score.buy_in(user1)
    user_input = input("Enter your choice\nSlots (1) - Roulette (2) - Quit (q): ")
    print(user1.funds)
    if user_input == '1':
        print("Option 1 selected")
        slots_game = Slots(score)  # Pass the score object to the Slots class
        slots_game.welcome()
        slots_game.run(user1)
    elif user_input == '2':
        print("Option 2 selected")
        roulette_game = Roulette(score)  # Pass the score object to the Slots class
        roulette_game.welcome()
        roulette_game.run(user1)
    elif user_input.lower() == 'q':
        print("Exiting the loop")
        score.reorganize_scores()
        break
    
    else:
        print("Invalid input. Please enter 1, 2, or q.")
