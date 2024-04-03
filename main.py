#Modules
from deck_of_cards import deck_of_cards
import time

deck_obj = deck_of_cards.DeckOfCards()
#Card class

class Card:
    def __init__(self, value):
        self.value = value

#Player class
class Player:
    def __init__(self, name):
        self.name = name

#Game class
class Game:
    def __init__(self):
        self.player = Player("Me")
        self.computer = Player("Computer")
        self.mode = None

# choose mode of an app (regular, opposite)
   
    def gamemode(self):
        mode = input("Which mode would you like to play? Enter 'R' for regular and 'O' for opposite: ")
        self.mode = 'R' if mode == 'R' else 'O'

    
# dealing cards
    def deal_cards(self):
        deck_obj.shuffle_deck()
        self.player = deck_obj.give_random_card()
        self.computer = deck_obj.give_random_card()


# countdown
    def countdown(self):
        print("Countdown")
        for i in range(3, 0, -1):
            print (i)
            time.sleep(1)
        
# winner loser
    def winnerloser(self):
        print (f"Player's card: {self.player.name}")
        print (f"Computer's card: {self.computer.name}")

        if self.mode == "R":
            if self.player.value > self.computer.value:
                print ("Player wins")
            elif self.player.value < self.computer.value:
                print ("Computer wins")
            else:
                print ("Its a tie")
        elif self.mode == 'O':
            if self.player.value < self.computer.value:
                print ("Player wins")
            elif self.player.value > self.computer.value:
                print ("Computer wins")
            else:
                print ("Its a tie")

    def play(self):
        self.gamemode()
        self.deal_cards()
        self.countdown()
        self.winnerloser()

def main():
    game = Game()
    game.play()




if __name__ == "__main__":
    main()    