#Modules
from deck_of_cards import deck_of_cards
import time
import sys

deck_obj = deck_of_cards.DeckOfCards()
#Card class

class Card:
    def __init__(self, value):
        self.value = value

#Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

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
        self.player_card = deck_obj.give_random_card()
        self.computer_card = deck_obj.give_random_card()


# countdown
    def countdown(self):
        print("Countdown")
        for i in range(3, 0, -1):
            print (i)
            time.sleep(1)
        
# winner loser
    def winnerloser(self):
        print (f"Player's card: {self.player_card.name}")
        print (f"Computer's card: {self.computer_card.name}")
        if self.mode == "R":
            if self.player_card.value > self.computer_card.value:
                self.player.wins += 1
                print ("Player wins")
            elif self.player_card.value < self.computer_card.value:
                self.computer.wins += 1
                print ("Computer wins")
            else:
                print ("Its a tie")
        elif self.mode == 'O':
            if self.player_card.value < self.computer_card.value:
                self.player.wins += 1
                print ("Player wins")
            elif self.player_card.value > self.computer_card.value:
                self.computer.wins += 1
                print ("Computer wins")
            else:
                print ("Its a tie")


        print(f"Score - Player: {self.player.wins}, Computer: {self.computer.wins}")
        self.announce_game_winner()        

    def announce_game_winner(self):
        if self.player.wins == 5:
            print ("Player wins the game!")
        elif self.computer.wins == 5:
            print ("Computer wins the game")
    
    def continue_game(self):
        if self.player.wins > self.computer.wins:
            print("Player wins the game!")
        elif self.player.wins < self.computer.wins:
            print("Computer wins the game!")
        else:
            print("It's a tie!")

    def continue_game1(self):
        # Ask user to continue, handle end-of-game scenarios
        try:
            if input("Do you want to continue? (Y/N) ").upper() == 'Y':
                return True
            else:
                self.continue_game()
                return False
        except EOFError:
            print("Game interrupted!")
            self.continue_game()
            return False
        

    def play(self):
        self.gamemode()
        while self.player.wins < 5 and self.computer.wins < 5:
            self.deal_cards()
            self.countdown()
            self.winnerloser()
            if not self.continue_game1():
                break

def main():
    game = Game()
    game.play()




if __name__ == "__main__":
    main()    