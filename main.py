

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-", "-", "-"],
]
user = True
turns = 0
def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} " , end="")
        print()


def quit(user_input):
    if user_input.lower() == "q": print("dzieki za gre"); return True
    else: return False
def check_input(user_input):
    if not isnum(user_input): return False
    user_input = int(user_input)
    return True
def isnum(user_input):
    if not user_input.isnumeric():
        print("tthis is not a number")
    else: return True
def bounds(user_input):
    if user_input>9 or user_input<1:
        print("This number is out of bounds")
        return False
    else: return True
def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] !="-":
        print("zajete")
        return True
    else: return False
def coordinates(user_input):
    row = int(user_input/3)
    col = user_input
    if col> 2: col = int(col%3)
    return (row, col)
def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col]= active_user
def curus(user):
    if user == True: return "x"
    else: return "o"
def checkrow(user,board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False
def checkcol(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False
def checkdiag(user,board):
    if board[0][0] == user and board[1][1]== user and board[2][2]==user:
        return True
    elif board[0][2] == user and board[1][1]== user and board[2][0]==user:
        return True



def iswin(user, board):
    if checkrow(user, board): return True
    if checkcol(user,board): return True
    if checkdiag(user,board): return True
while turns<9:
    active_user = curus(user)
    print_board(board)
    user_input = input("wybierz od 1 do 9 albo wybierz\"q\" aby wyjść" +"")
    if quit(user_input):break
    if not check_input(user_input):
        print("Sproboj ponownie")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("please try again")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
       print(f"{active_user.upper()} won! ")
       print_board(board)
       break
    turns += 1
    if turns ==9:
        print("tie")
    user = not user