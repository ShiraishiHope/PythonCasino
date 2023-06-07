#! usr/bin/env python3

from User import User
from Score import Score

score = Score()

name = input("name: ")

user1 = User(name)

score.check_user(user1)
score.reorganize_scores()

