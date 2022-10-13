import numpy as np
import random
class Auction:

    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders
        self.balances = {bidder:0 for bidder in bidders}

    def execute_round(self):
        


class User:

    def __init__(self):
        self.__probability = np.random.uniform(0, 1)

    def show_ad(self):
        return np.random.uniform(0, 1) < self.__probability
