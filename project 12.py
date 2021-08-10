from math import ceil, floor


def getSummed(n):
    return n*(n+1)>>1# b9inary shift lol

numbers = []
n = 0
t=0
while len(numbers) <= 500:
    numbers = []
    n += 1
    sumed = getSummed(n)
    for i in range(1,ceil(sumed/2)):
        if sumed %i == 0:
            numbers.append(i)
            if (int(sumed/i) not in numbers):
                numbers.append(int(sumed/i))
    if len(numbers)>t:
        t=len(numbers)
        print(t)
        
print(n)
print(sumed)
