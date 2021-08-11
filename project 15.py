import random
length=20

arrPaths=[]
for i in range(0,100000):
    thisPath=[]
    down=0
    right=0
    while down!=length  or right!=length:
        if down!=length and right!=length:
            r = random.randrange(0,2)
            thisPath.append(r)
            if r==0:
                down+=1
            else:
                right+=1 
        elif down==length:
            thisPath.append(1)
            right+=1
        else:
            thisPath.append(0)
            down+=1
    if thisPath not in arrPaths:
        arrPaths.append(thisPath)

print(len(arrPaths))
