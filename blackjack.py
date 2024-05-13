'''
Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
Money: 5000
How much do you bet? (1-5000, or QUIT)
> 400
Bet: 400
'''
import random
class BlackJack():
    def __init__(self):
        self.money = 5000
        self.round = 0
        self.player = {0: [], 1: []}
        self.turn = 0
        self.lastPassed = False

    def deal(self):
        play = True
        print('Current money:', str(self.money))
        inpp = input('How much do you bet? (1-5000, or QUIT)')
        if inpp.lower() == 'quit':
            play = False
        bet = int(inpp)
        while play:
            if self.turn == 1:
                if sum(self.player[1]) >= 17:
                    print('Opponent pass ')
                    if self.lastPassed:
                        self.decide(bet)
                        self.player[1] = []
                        self.player[0] = []
                    else:
                        self.turn = 0
                        self.lastPassed = True
                else:
                    val = random.randint(2, 11)
                    self.turn = 0
                    self.lastPassed = False
                    print('Opponent deal:', str(val))
                    self.player[1].append(val)
                    if sum(self.player[1]) > 21:
                        print('Busted, player won ')
                        self.money += bet
                        print('You have', self.money)
                        self.player[1] = []
                        self.player[0] = []
            else:
                inp = input('Would you like to hit (H) or stand (S)')
                if inp.lower() == 's':
                    self.turn = 1
                    print('You decided to pass')
                    if self.lastPassed:
                        self.decide(bet)
                        self.player[1] = []
                        self.player[0] = []
                    self.lastPassed = True
                else:
                    self.turn = 1
                    self.lastPassed = False
                    val = random.randint(2, 11)
                    print('You decided to deal:', str(val))
                    self.player[0].append(val)
                    if sum(self.player[0]) > 21:
                        print('Busted, you lost')
                        self.money -= bet
                        print('You have', self.money)
                        self.player[1] = []
                        self.player[0] = []

    def decide(self, bet):
        if sum(self.player[1]) > sum(self.player[0]):
            print('You lost, opponent has', self.player[1], 'you have', self.player[0])
            self.money -= bet
            print('You have', self.money)
        elif sum(self.player[1]) < sum(self.player[0]):
            print('You won, opponent has', self.player[1], 'you have', self.player[0])
            self.money += bet
            print('You have', self.money)
        else:
            print('draw, opponent has', self.player[1], 'you have', self.player[0])
            print('You have', self.money)


player = BlackJack()
player.deal()