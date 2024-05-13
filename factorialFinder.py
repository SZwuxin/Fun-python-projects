def factorialFinder(num):
    allFactor = []
    if num == 0:
        return []
    if num == 1:
        return [1]
    for i in range(1, int(num**0.5)):
        if num % i == 0:
            allFactor.append(i)
            allFactor.append(num//i)
    allFactor.sort()
    return allFactor

inp = input('Enter an integer greater than 0')
print(factorialFinder(int(inp)))