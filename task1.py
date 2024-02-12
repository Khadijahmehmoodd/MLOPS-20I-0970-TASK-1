import random

#display game board
def displayGameBoard(gameBoard):
   
    for i in range(9):
       
        if i % 3 == 0 and i != 0:
          
            print("_____________________")
        
        for j in range(9):
           
            if j % 3 == 0 and j != 0:
              
                print("| ", end="")
           
            if j == 8:
               
                print(gameBoard[i][j])
         
            else:
               
                print(str(gameBoard[i][j]) + " ", end="")
  
    print()

    # solved board

def solutionOfGameBoard(gameBoard):
    
    check = checkIfEmpty(gameBoard)
    
    if not check:
        
        return True
  
    else:
       
        row, column = check

  
    for number in random.sample(range(1, 10), 9):
        
        if checkIfValid(gameBoard, number, (row, column)):
           
            gameBoard[row][column] = number

          
            if solutionOfGameBoard(gameBoard):
               
                return True

            gameBoard[row][column] = 0

  
    return False

# check validilty
def checkIfValid(gameBoard, number, position):
    
  
    for i in range(len(gameBoard[0])):
      
       
        if gameBoard[position[0]][i] == number and position[1] != i:
           
            return False

   
    
    for i in range(len(gameBoard)):
      
       
        if gameBoard[i][position[1]] == number and position[0] != i:
            
           
            return False

   
    x_Axis = position[1] 
    
    y_Axis = position[0] 

    for i in range(y_Axis*3, y_Axis*3 + 3):
        
        for j in range(x_Axis * 3, x_Axis*3 + 3):
           
            if gameBoard[i][j] == number and (i,j) != position:
              
                return False

    return True
# check if the board is empty

def checkIfEmpty(gameBoard):
    
    for i in range(len(gameBoard)):
       
        for j in range(len(gameBoard[0])):
         
            if gameBoard[i][j] == 0:
              
                return (i, j)
   
    return None
# generates game board

def GameBoardGenerated(totalDisplacedCells):
   
    gameBoard = [[0 for j in range(9)] for i in range(9)]
    
    solutionOfGameBoard(gameBoard)

   
    cellsToBeDisplaced = totalDisplacedCells
   
    while cellsToBeDisplaced > 0:
       
        row = random.randint(0, 8)
       
        column = random.randint(0, 8)
      
        if gameBoard[row][column] != 0:
           
            gameBoard[row][column] = 0
           
            cellsToBeDisplaced -= 1

   
    return gameBoard


if __name__ == '__main__':
    
    try:
      
        totalDisplacedCells = 9
       
        if totalDisplacedCells < 1 or totalDisplacedCells > 81:
          
            raise ValueError("Displaced Cells' numberber must be between 1 and 81")
   
    except ValueError as e:
       
        exit()

    gameBoard = GameBoardGenerated(totalDisplacedCells)
    
    print("Generated gameBoard:")
    print("")
   
    displayGameBoard(gameBoard)


   
    game_board = [row[:] for row in gameBoard]
   
    solutionOfGameBoard(game_board)
    

    
    print("solutionOfGameBoardd gameBoard:")
    print("")
   
    displayGameBoard(game_board)
