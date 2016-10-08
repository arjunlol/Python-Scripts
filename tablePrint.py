#! python3
#tablePrint - takes in list and prints formatted list
uglist = [['apples','oranges','cherries','banana'],
          ['Alice','Bob','Carol','David'],
          ['dogs','cats','moose','goose']]

def printTable(uglyList):
    colWidths = [0]*len(uglyList)
    for j in range(len(colWidths)):
        for i in range(len(uglyList[j])):
            if colWidths[j] < len(uglyList[j][i]):
                colWidths[j]=len(uglyList[j][i])

    for x in range(len(uglyList[0])):
        for y in range(len(uglyList)):
            print(uglyList[y][x].rjust(colWidths[y]), end =" ")
        print()
printTable(uglist)

