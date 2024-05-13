def collatz(num):
    count = 0
    while True:
        if num == 1:
            print('Success, reached 1 after', str(count), 'tries')
            break
        elif num % 2 == 0:
            num /= 2
        else:
            num*=3
            num+=1
        count += 1

try:
    collatz(int(input('Please enter an integer: ')))
except Exception:
    print('Invalid input')

