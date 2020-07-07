#! python3
# printTable.py - Takes a list of list of strings and displays it in
# a well organised table (right-justified)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    count = 0
    table = ''
    for i in tableData:
        maxLen = 0
        for j in i:
            if maxLen < len(j):
                maxLen = len(j)
        colWidths[count] = maxLen
        count += 1
    #print(colWidths) #Test
    #for i in tableData:
    count = 0
    while count < len(i):
        outerCount = 0
        while outerCount < len(tableData):
            data = tableData[outerCount][count]
            table = table + data.rjust(colWidths[outerCount])
            outerCount += 1
        table = table + '\n'
        count += 1
    print(table)


printTable(tableData)
            