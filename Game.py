from Deck import Deck
from Player import Player

class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.players = [Player(user=x % 2 == 0, name=("Player") if x % 2 == 0 else "Bot") for x in range(players)]
        self.play()

    def deal(self, player):
        player.hands.add_card(self.deck.draw(player))

        
    def shuffle(self):
        self.deck.shuffle()

    def find_winner(self, player1, player2):
        if player1.get_value() > player2.get_value():
            player1.score += 1
        elif player2.get_value() > player1.get_value():
            player2.score += 1

    def display_final(self):
        print(f"\nFINAL TALLY:\n")
        print(f"{'Player:':<10}{self.players[0].score}")
        print(f"{'Computer:':<10}{self.players[1].score}\n")
        if self.players[0].score == self.players[1].score:
            print("TIE GAME")
        else:
            print(f"YOU {'WIN' if self.players[0].score > self.players[1].score else 'LOSE'}")

    def play(self):
        self.shuffle()
        while True:
            if len(self.players[0].hands.hand) < 26:
                for i in range(2):
                    self.deal(self.players[i])
                self.find_winner(self.players[0], self.players[1])
                for player in self.players:
                    player.print_hand()
                user_choice = input("Play again? (y/n) \n>")
                if user_choice.lower() == 'n':
                    self.display_final()
                    break
            else:
                print("Deck is empty, reshuffling.")
                for i in range(2):
                    self.players[i].hands.hand = []
                self.deck = Deck()
                self.shuffle()
            

if __name__ == "__main__":
    game = Game(2)
