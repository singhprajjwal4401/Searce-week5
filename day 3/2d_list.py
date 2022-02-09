#two dimensional list

def getMatrix():
    matrix = []

    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))
    for row in range(numberOfRows):
        matrix.append([])
        for column in range(numberOfColumns):
            value = eval(input("enter a value and press enter: "))
            matrix[row].append(value)
    return matrix

def accumulate(m):
    total=0
    for row in m:
        total += sum(row)
    return total

def main():
    m=getMatrix()
    print(m)

    print("\nSum of all elements is ", accumulate(m))

main()
