def checkMainDiagonal(list_):
    sum_=0
    for each in list_:
        sum_=sum_+int(each)
    return sum_

def checkDiagonal(list_):
    sum0 = 0
    for each in list_:
        sum0 = sum0 + int(each)
    return sum0
  
def checkRows(row):
    sum1=0
    for elem in row:
        sum1=sum1+int(elem)
    return sum1

def checkColumns(column):
    sum1=0
    for elem in column:
        sum1=sum1+int(elem)
    return sum1

def isMagic(nam1,nam2):
    f=open(nam1,"r")
    number_of_inputs=int(f.readline())
    f.readline()
    size=int(f.readline())
    print(size)
    rowlist=[]
    columnList=[]
    listOfLists=[]
    
    for i in range(size):
        line=f.readline()
        current_row=line.split()
        listOfLists.append(current_row)
        rowlist.append(checkRows(listOfLists[i]))
    print(rowlist)
    print(listOfLists)
    for i in range(size):
        current_column=[]
        for j in range(size):
            current_column.append(listOfLists[j][i])
        print(current_column)
        columnList.append(checkColumns(current_column))
    print(columnList)

               

def main():
    name1=input("Enter name of input file:")
    name2=input("Enter name of output file:")
    if name1==name2:
        print("The names are the same")
    else:
        isMagic(name1,name2)
        print("The output has been written to results.txt")
main()


