from random import shuffle

class Card:
    suits = ['spades', 'heart', 'diamond', 'clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, s, v):
        self.suit = s
        self.value = v

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(j, i))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.cards = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("Player1 Name: ")
        name2 = input("Player2 Name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def Wins(self, winner):
        w = "{} wins the round"
        w = w.format(winner)
        print(w)

    def draw(self, pn1, pc1, pn2, pc2):
        d = "{} drew {}, {} drew {}"
        d = d.format(pn1, pc1, pn2, pc2)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any key to play: "
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.Wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.Wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p2.wins > p1.wins:
            return p2.name
        return "It was a tie"


game = Game()
game.play_game()
