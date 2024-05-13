import random


def diceRoller(roll):
    res = 0
    if '+' in roll:
        sp = roll.split('+')
        before, after = sp[0].split('d')[0], sp[0].split('d')[1]
        for i in range(int(before)):
            rand = random.randint(1, int(after))
            res += rand
        res += int(sp[1])
    elif '-' in roll:
        sp = roll.split('-')
        before, after = sp[0].split('d')[0], sp[0].split('d')[1]
        for i in range(int(before)):
            rand = random.randint(1, int(after))
            res += rand
        res -= int(sp[1])
    else:
        before, after = roll.split('d')[0], roll.split('d')[1]
        for i in range(int(before)):
            rand = random.randint(1, int(after))
            res += rand
    return res

inp = input('input a valid dice roll, example: 12d6-1, 6d14+2')
print(diceRoller(inp))