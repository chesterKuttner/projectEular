odd = lambda n : int(3*n+1)
even= lambda n : int(n/2)

top=[0,0]
for i in range(1,1000000):
    x=i
    time=0
    while x != 1:
        time+=1
        if x % 2 == 0:
            x=even(x)
        else:
            x=odd(x)
    if time>top[1]:
        top=[i,time]
print(top)    