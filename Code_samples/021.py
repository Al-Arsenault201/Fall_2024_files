#multi-level lists from October 21
from tarfile import TruncatedHeaderError


#we're going to build a list
# but the elements of the list are themselves lists
def get_input():
    size = int(input("enter how many rows"))
    data = []
    for i in range(size):
        data.append(input("enter the next row"))
#    print(data)
    for i in range(len(data)):
        data[i] = list(data[i])
    print(data)
    return data

def check_rows(game_board):
    #check each row in the 2-d list
    #if there are four x's in a row, return True
    #otherwise return False

    # in a 2-d list, an element is game_board[row][column]
    # if you only use one subscript, that's the whole row
    #check all rows
    for i in range(len(game_board)):
     #   to check one row
        print(i)
        for j in range(0,len(game_board[0])-4, 1):

            if game_board[i][j] == 'x' and game_board[i][j+1] == 'x' and game_board[i][j+2] == 'x' and game_board[i][j+3] == 'x':
                return True
    return False  #returned only because we've checked all rows

#you must use a loop to process a column
def check_columns(game_board):
    #define a column number
    for column in range(len(game_board[0])):
        #to check all the rows put another nested for loop below
        if game_board[0][column] == 'x' and game_board[1][column] == 'x' and game_board[2][column] == 'x' and game_board[3][column] == 'x':
            return True
    return False

if __name__ == "__main__":
    data = get_input()
    print("row match", check_rows(data))
    print("column match", check_columns(data))


