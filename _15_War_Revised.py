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
            return self.suit < c2.suit
        return False  # self.vaue > c2.value

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False  # self.value < c2.value

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)  # Shuffle all cards.

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()  # Select the last card in "self.cards" which was shuffled already, and remove that from "self.cards".

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

    def print_winner(self, winner):
        print("{} won this round!".format(winner))

    def print_draw(self, p1n, p1c, p2n, p2c):
        print("{} took {}, {} took {}.".format(p1n, p1c, p2n, p2c))

    def play_game(self):
        cards = self.deck.cards
        print("Start the war!")
        while len(cards) >= 2:
            response = input("Press q to end the war, other key to start next game.: ")
            if response == "q":
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            if self.p1.card > self.p2.card:
                self.p1.wins += 1  # Counter
                self.print_winner(self.p1.name)  # Display message.
            else:
                self.p2.wins += 1  # Counter
                self.print_winner(self.p2.name)  # Display message.
            print("\n")

        win = self.winner(self.p1, self.p2)
        print("All games finhsed, {}".format(win))
        print(self.p1.name + ": " + str(self.p1.wins))
        print(self.p2.name + ": " + str(self.p2.wins))
        print("\n")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name + "won!"
        if p1.wins < p2.wins:
            return p2.name + "won!"
        return "draw!"

game = Game()
game.play_game()
