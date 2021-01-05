from Piece import CheckerPiece
from Validator import MoveValidator

class CheckerGame:
    def __init__(self, color = "Black"):
        self.currentColor = color
        self.board = self.getBoard()
        self.moveValidator = MoveValidator()
        
    def getBoard(self, width = 8, height = 8):
        board = [[""] * width] * height
        return board
    
    def takeTurn(self, moves):
        isValidMove = True
        
        for move in range(moves-1):
            startPos, endPos = moves[move], moves[move+1]
            
            if self.moveValidator.isInvalid(self.board, startPos, endPos):
                isValidMove = False
                
        if not isValidMove:
            print("Invalid move")
            return
        else:
            self.updateBoard(moves)
        
        if self.currentColor == "Black":
            self.currentColor = "White"
        else:
            self.currentColor = "Black"
            
    def updateBoard(self, moves):
        pass
    
if __name__ == "__main__":
    game = CheckerGame()