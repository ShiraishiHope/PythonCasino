class Game:
    def __init__(self, game_name):
        self.game_name = game_name
    
    def welcome(self):
        print(f"Welcome to the {self.game_name}!")
