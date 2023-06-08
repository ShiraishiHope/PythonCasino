#! usr/bin/env python3

class User:
    def __init__(self, name):
        self.name = name
        
    def user_funds(self, funds):
        if funds > 0:
            self.funds = 0
            self.funds += funds
        else:
            raise ValueError("You need money to play at a casino")
    def update_funds(self, funds):
            self.funds += funds
        