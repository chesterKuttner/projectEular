
# import re
# r1 = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
# r2 = "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
# r3 = "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
# r4 = "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
# r5 = "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"
# r6 = "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
# r7 = "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
# r8 = "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
# r9 = "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
# r10 = "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"
# r11 = "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
# r12 = "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
# r13 = "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
# r14 = "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
# r15 = "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"
# r16 = "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
# r17 = "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
# r18 = "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
# r19 = "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
# r20 = "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
# grid = []
# grid.append(r1)
# grid.append(r2)
# grid.append(r3)
# grid.append(r4)
# grid.append(r5)
# grid.append(r6)
# grid.append(r7)
# grid.append(r8)
# grid.append(r9)
# grid.append(r10)
# grid.append(r12)
# grid.append(r13)
# grid.append(r14)
# grid.append(r15)
# grid.append(r16)
# grid.append(r17)
# grid.append(r18)
# grid.append(r18)
# grid.append(r19)
# grid.append(r20)
# for i in range(1, 20):
#     grid[i] = '['+re.sub("\s+", ",", grid[i].strip())+'],'
#     print(grid[i])

grid = [[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71,
            40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24,
            68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92,
        36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33,
            53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38,
        40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63,
            94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78,
        78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35,
        14, 00, 61, 33, 97, 34, 31, 33, 95],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88,
        24, 00, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44,
            37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73,
            92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57,
            32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33,
        67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94,
            72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62,
        99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62,
        99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31,
            49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
t = 0
h = 0
for y in range(0, 19):
    for x in range(0, 19):

        t += grid[y][x]
        h += 1
average = t/h
print(average)

# [1,2,3,4]
# [1,2,3,4]
# [1,2,3,4]
# [1,2,3,4]


def checkSimilar(index1, index2):

    # if (index1[0] <= (index2[0]+3) and index1[0] >= (index2[0]-3)) and (index1[1] <= (index2[1]+3) and index1[1] >= (index2[1]-3)):
    #     return True
    # else:
    #     return False

    if index1[0] == index2[0] and ((index1[1] <= (index2[1]+3)) and (index1[1] >= (index2[1]-3))):
        return True

    if index1[1] == index2[1] and ((index1[0] <= (index2[0]+3)) and (index1[0] >= (index2[0]-3))):
        return True
    if (abs(index1[0]-index2[0]) == abs(index1[1]-index2[1])) and (abs(index1[1]-index2[1]) <= 3):
        return True

    return False


aboveAvrgGrid = []
for y in range(0, 19):
    for x in range(0, 19):
        if grid[y][x] > average:
            aboveAvrgGrid.append([y, x])

topCandidates = []
for y in range(0, len(aboveAvrgGrid)):
    count = 0
    for two in range(0, len(aboveAvrgGrid)):

        if checkSimilar(aboveAvrgGrid[y], aboveAvrgGrid[two]):
            count += 1

    count -= 1
    if count >= 3:
        topCandidates.append([y, count])
topCandidates = sorted(topCandidates, key=lambda x: x[1], reverse=True)

print(topCandidates)
print(len(topCandidates))


def calculateGrid(yOrigin, xOrigin):
    gTotal = 0
    if yOrigin < 16:
        t = 1       
        for y in range(yOrigin, yOrigin+3):
            t *= grid[y][xOrigin]
        if t > gTotal:
            gTotal = t
    if xOrigin < 16:
        t = 1
        for x in range(xOrigin, xOrigin+3):
            t *= grid[yOrigin][x]
        if t > gTotal:
            gTotal = t
    if xOrigin > 3:
        t = 1
        for x in range(xOrigin-3, xOrigin):
            t *= grid[yOrigin][x]
        if t > gTotal:
            gTotal = t
    if yOrigin > 3:
        t = 1
        for y in range(yOrigin-3, yOrigin):
            t *= grid[y][xOrigin]
        if t > gTotal:
            gTotal = t
    if yOrigin > 3 and xOrigin > 3:
        t = 1
        for c in range(1, 3):
            t *= grid[yOrigin-c][xOrigin-c]
        if t > gTotal:
            gTotal = t
    if yOrigin < 16 and xOrigin < 16:
        t = 1
        for c in range(1, 3):
            t *= grid[yOrigin+c][xOrigin+c]
        if t > gTotal:
            gTotal = t
    return gTotal


top = 0
temp = 0
for i in range(0, len(topCandidates)):
    temp = calculateGrid(*aboveAvrgGrid[topCandidates[i][0]])
    if temp > top:
        top = temp

print(top)
# 70600674
