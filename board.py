board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def valid(b,num,position):

    #check for the row
    for i in range(len(b[0])):
        if b[position[0]][i] == num and position[1] != i:
            return False

    #check for the column
    for i in range(len(b)):
        if b[i][position[1]] == num and position[0] != i:
            return False

    #check for the box condition
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):      
            if  b[i][j] == num  and  position != (i,j) :
                return False

    return True            

def solve(b):
    find = empty_square(b)
    if not find:
        return True
    else:
        row,column = find
    for i in range(1,10):
        if valid(b,i,(row,column)):
            b[row][column] = i 

            if solve(b):
                return True

            b[row][column] = 0

    return False               








def sudokudesign(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("-------------------")
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print("|", end = "")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end = "")     


def empty_square(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j)


    return None



 
print(sudokudesign(board))
solve(board) 
print("-----------------------")
print(sudokudesign(board))
