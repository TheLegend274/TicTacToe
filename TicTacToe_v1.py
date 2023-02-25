#    0.  1.  2
# 0 [ ] [ ] [ ]
# 1 [ ] [ ] [ ]
# 2 [ ] [ ] [ ]

#Get the user inputs
player1Mark = input("Please choose X or O")
if player1Mark == "X":
  player2Mark = "O"
else:
  player2Mark = "X"

#Made a empty list to create a board using a for loop

board = []
for row in range(3):
  board.append([""] * 3)

#Checks if the user input is valid or not
#If its greater than 3 its not valid and returns to the board an empty string

def isValid(row, col):
  if not (row >= 0 and row < 3 and col >= 0 and col < 3):
    return False

  return board[row][col] == ""

#While the players move is not isValidMove it keeps on asking to input
#If the user inputs the wrong number it will say to enter  a valid move
def playerMakeMove(mark):
  isValidMove = False

  while not isValidMove:
    inputRow = int(input("Please pick a row"))
    inputColumn = int(input("Please pick a column"))

    isValidMove = isValid(inputRow, inputColumn)
    if not isValidMove:
      print("Please enter a valid input")

  board[inputRow][inputColumn] = mark

#checks if the horizontal of the board is empty or not
def checkHorizontal():
  for row in range(3):
    mark = board[row][0]
    if mark == "":
      continue

    matches = 1
    for col in range(1, 3):
      if mark == board[row][col]:
        matches += 1
    
    if matches == 3:
      return True

  return False

#Checks vertically if there is a empty spot or  not 
def checkVertical():
  for col in range(3):
    mark = board[0][col]    
    if mark == "":
      continue

    matches = 1
    for row in range(1, 3):
      if mark == board[row][col]:
        matches += 1

    if matches == 3:
      return True

  return False

#Checks diagonly if the board is empty or not 
def diagonal(row, col, increment):
  mark = board[row][col]
  if mark == "":
    return False
  
  matches = 1
  for _ in range(2):
    row += increment
    col += increment
    if mark == board[row][col]:
      matches += 1
  
  return matches == 3
#checks the digonal of the board
def checkDiagonal():
  return diagonal(0, 0, 1) or diagonal(0, 2, -1)

#Checks the winner by seeing if they filled out the spot according to the 3 functions 
def checkWinner():
  return checkHorizontal() or checkVertical() or checkDiagonal()
#Checks if the board is filled
def checkBoardFilled():
  for row in range(3):
    for col in range(3):
      if board[row][col] == "":
        return False
  return True

#prints out who won and Game over if the board is felled 
def ticTacToe():
  while True:
    for mark in [player1Mark, player2Mark]:
      playerMakeMove(mark)

      for row in range(3):
        print(board[row])

      if checkWinner():
        print(mark, "wins!")
        return

      if checkBoardFilled():
        print("Game over")
        return

ticTacToe()


