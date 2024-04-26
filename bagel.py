import random
class Bagel():
    def __init__(self):
        self.number = random.randint(100,999)
        self.guessNum = 0
        self.text = '''
                Bagels, a deductive logic game.
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
      Pico         One digit is correct but in the wrong position.
      Fermi        One digit is correct and in the right position.
      Bagels       No digit is correct.
    I have thought up a number.
     You have 10 guesses to get it.
                '''
    def guess(self):
        if self.guessNum == 0:
            print(self.text)
            self.text = ''
        res = ''
        inp = input("Guess #" + str(self.guessNum) + ": ")
        try:
            int(inp)
        except ValueError:
            print('Unsupported input, try again')
            self.guess()
        if int(inp) > 999 or int(inp) < 100:
            print('Unsupported input, try again')
            self.guess()
        if int(inp) == self.number:
            print("You won :)")
        else:
            for i in range(len(inp)):
                if inp[i] == str(self.number)[i]:
                    res += 'Fermi '
                elif inp[i] in str(self.number):
                    res+= 'Pico '
            if res == '':
                res = 'Bagel'
            print(res)
            self.guessNum += 1
            if self.guessNum > 10:
                print("You lost :(, the number I'm thinking of is:", str(self.number))
            else:
                self.guess()


p = Bagel()
p.guess()
