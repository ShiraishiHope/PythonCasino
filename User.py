#! usr/bin/env python3

import hashlib

class User:
    def __init__(self, name):
        self.name = name
        self.password = None
        
    def set_password(self,password):
        self.password = hashlib.sha512(password.encode()).hexdigest()
        
    def user_funds(self, funds):
        if funds > 0:
            self.funds = 0
            self.funds += funds
        else:
            raise ValueError("You need money to play at a casino")
    def update_funds(self, funds):
            self.funds += funds
        