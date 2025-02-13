from game_utils import *

class GameState:
    def __init__(self, turn = 1, board = None, piecesLeft = None):
        if turn < 1:
            raise ValueError
        self._turn = 1

        self._board = [[0 for x in range(COLS)] for x in range(ROWS)]
        if board:
            for row in range(ROWS):
                for col in range(COLS):
                    if 0 > board[row][col] or board[row][col] > 4:
                        raise ValueError
                    self._board = board[row][col]

        self._piecesLeft = {}
        if piecesLeft:
            for player in [1,2,3,4]:
                self._piecesLeft[player] = list(piecesLeft[player])
        else:
            for player in [1,2,3,4]:
                self._piecesLeft[player] = list(PIECES.keys())

    @property
    def turn(self):
        return self._turn
    
    @property
    def board(self):
        return self._board
    
    @property
    def piecesLeft(self):
        return self._piecesLeft
    
    def applyMove(self, move):
        self._turn += 1

        if move == None:
            return

        if not move.isLegal(self):
            raise InvalidMove
        # TODO apply the move to the board

    def clone(self):
        clone = GameState(self.turn, self.board, self.piecesLeft)

    def __str__(self):
        return string(self.turn) # TODO
