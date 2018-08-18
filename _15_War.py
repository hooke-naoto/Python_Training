from random import shuffle

class Card:

    # Suits in order of weakness.
    suits = ["spades", "hearts", "diamonds", "clubs"]

    # Values in order of weakness.
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """ suits and values are integer """
        self.value = v
        self.suit = s

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False  # self.vaue > c2.value

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False  # self.value < c2.value

# card1 = Card(10, 2)  # 10 of diamonds
# card2 = Card(11, 3)  # 3 of clubs
# print(card1)
# print(card2)
# print (card1 < card2)

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)  # Shuffle all cards.

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()  # Select the last card in "self.cards" which was shuffled already, and remove that from "self.cards".

# deck = Deck()
# for card in deck.cards:
#     print(card)

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

class Game:
    def __init__(self):
        name1 = input("Name of player1: ")
        name2 = input("Name of player2: ")
        self.deck = Deck()
        self.p1 = Player(name1)  # Object Player() is added as an instance variable to object Game().
        self.p2 = Player(name2)

    def wins(self, winner):
        print("{} won this round!".format(winner))

    def draw(self, p1n, p1c, p2n, p2c):
        print("{} took {}, {} took {}.".format(p1n, p1c, p2n, p2c))

    def play_game(self):
        cards = self.deck.cards
        print("Start the war!")
        while len(cards) >= 2:
            response = input("Press q to end the war, other key to start next game.: ")
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1  # Counter
                self.wins(self.p1.name)  # Display message.
            else:
                self.p2.wins += 1  # Counter
                self.wins(self.p2.name)  # Display message.

        win = self.winner(self.p1, self.p2)
        print("All games finhsed, {} won!".format(win))
        print(self.p1.name + ": " + str(self.p1.wins))
        print(self.p2.name + ": " + str(self.p2.wins))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Draw!"

game = Game()
game.play_game()
