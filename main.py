import math
def main():
    createMulTable(9,9)

def createMulTable(row,column):
    valuelist = calculateMulValue(row,column)
    printLine(row,column,valuelist)
    print('\n')

def printLine(row,column,valuelist):
    printItem(row,column,valuelist) 
    if (column-1 != 0):
        print('\n') 
        printLine(row,column-1,valuelist)

def printItem(row,column,valuelist):
    if (str(row)+str(column)) in valuelist:
        print(row,'*',column,'=',valuelist[str(row)+str(column)],end=' ')
        if (row-1 != 0):
            printItem(row-1,column,valuelist)
    else:
        print(row,'*',column,'=',valuelist[str(column)+str(row)],end=' ')
        if (row-1 != 0):
            printItem(row-1,column,valuelist)


def calculateMulValue(row,column):
    valuelist = {}
    mul(row,column,valuelist)
    valuelist['11'] = 1
    return valuelist

def mul(row,column,valuelist):
    if row == 1:
        if (str(row)+str(column)) not in valuelist:
            if (str(column)+str(row)) not in valuelist:
                valuelist[str(row)+str(column)] = column
    if column == 1:
        if (str(column)+str(row)) not in valuelist:
            if (str(row)+str(column)) not in valuelist:
                valuelist[str(row)+str(column)] = row
    if row > 1 and column > 1:
        if (str(column)+str(row)) not in valuelist:
            if (str(row)+str(column)) not in valuelist:
                valuelist[str(row)+str(column)] = row * column
                mul(row-1,column,valuelist)
                mul(row,column-1,valuelist)
    
if __name__ == '__main__':
    main()