import numpy as np
import random
class Auction:

    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders
        self.balances = {bidder:0 for bidder in bidders}

    def execute_round(self):
        user = random.choice(self.users)
        bids = np.empty((len(self.bidders),1))
        for bidder in self.bidders:
            bids = np.append(bids, bidder.bid(user))
        winner = self.bidders[np.argmax(np.array(bids))]
        second_price = bids.sort()[-2]
        for bidder in self.bidders:
            if bidder == winner:
                clicked = user.show_ad()
                bidder.notify(True, second_price, clicked)
                self.balances[bidder] += (1-second_price) if clicked else -second_price
            else:
                bidder.notify(False, second_price, None)


class User:

    def __init__(self):
        self.__probability = np.random.uniform(0, 1)

    def show_ad(self):
        return np.random.uniform(0, 1) < self.__probability
