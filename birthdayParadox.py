import collections
import random


class birthdayParadox():
    def __init__(self, numberOfPeople, amountToSimulate):
        self.num = numberOfPeople
        self.amount = amountToSimulate
        self.numWithSameBirthday = 0

    def birthdayCount(self):
        n = self.amount
        while n > 0:
            dic = collections.defaultdict(int)
            for i in range(self.num):
                r = random.randint(1,365)
                if dic[r] >= 1:
                    self.numWithSameBirthday+=1
                    break
                dic[r] += 1
            n-=1
        print('After', str(self.amount), 'of runs, a total of', str(self.numWithSameBirthday/self.amount*100) + '% of runs have people with the same birthday')
num = input('How many birthdays shall I generate? (Max 100)')
amount = input('How many times shall I simulate? (Max 100000)')
try:
    if int(num) <= 100 and int(amount) <= 100000:
        birthdayParadox(int(num), int(amount)).birthdayCount()
    else:
        print('Incorrect input detected')
except Exception:
    print('Invalid input detected')
