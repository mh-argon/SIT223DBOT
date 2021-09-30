from Game import *

class ConnectFour(Game):
    name = "Number Guessing"
    alias = [name, "ConnectFour", "connect", "c4"]
    async def create(ctx, channel, user):
        return ConnectFour(ctx, channel, user)

    def __init__(self, ctx, channel, user):
        super().__init__(ctx, channel, user)
        # Create board[ROW][COLUMN]
        self.BOARD_ROWS = 6
        self.BOARD_COLUMNS = 7
        board = [[0 for i in range(self.BOARD_COLUMNS)] for i in range(self.BOARD_ROWS)]
        self.state = ConnectFourState(self, board, self.BOARD_ROWS, self.BOARD_COLUMNS)

class ConnectFourState(GameState):
    parent: ConnectFour
    def __init__(self, parent: ConnectFour, board, BOARD_ROWS, BOARD_COLUMNS):
        super().__init__(parent, 0)
        self.BOARD_ROWS = BOARD_ROWS
        self.BOARD_COLUMNS = BOARD_COLUMNS
        self.player_turn = 1
        self.board = board
        self.fin = False

    # TODO: implement 2nd player (invitation) or AI

    async def finished(self):
        if self.fin:
            if self.player_turn == 1 or self.player_turn == 2:
                return [self.parent.owner], "GG player {} wins!".format(self.player_turn)
            else: 
                return [self.parent.owner], "GG it's a draw"
        return False

    def to_string(self):
        board_string = "Now player {}'s turn\n".format(self.player_turn)
        # Loop through board rows backwards (board is printed from top to bottom)
        for r in range(self.BOARD_ROWS-1, -1, -1):
            for c in range(self.BOARD_COLUMNS):
                if self.board[r][c] == 0:
                    board_string += ":black_circle:"
                elif self.board[r][c] == 1:
                    board_string += ":red_circle:"
                elif self.board[r][c] == 2:
                    board_string += ":blue_circle:"
            board_string += "\n"
        board_string += ":one::two::three::four::five::six::seven:\n"
        board_string += "Enter the column number to place piece (1-7)"
        return board_string

    async def next(self):
        self.index += 1
        message, move = await self.parent.read_int()
        # If move successful:
        if self.board_move(move):
            # If player connected 4, end turn
            if self.check_board():
                self.fin = True
                return self
            # switch player turns
            if self.player_turn == 1:
                self.player_turn = 2
            else:
                self.player_turn = 1
        return self

    def board_move(self, move):
        move_idx = move-1
        # Check if valid column and column is not full
        if (move_idx < 0) or (move_idx >= self.BOARD_COLUMNS):
            return False
        elif (self.board[-1][move_idx] != 0):
            return False
        else: # Place piece in lowest vacant spot in the column
            for i in range(len(self.board)):
                if self.board[i][move_idx] == 0:
                    self.board[i][move_idx] = self.player_turn
                    return True
        return False

    def check_board(self):
        # Check for horizontal win
        for r in range(self.BOARD_ROWS):
            for c in range(self.BOARD_COLUMNS-3):
                if self.board[r][c] == self.player_turn and self.board[r][c+1] == self.player_turn and self.board[r][c+2] == self.player_turn and self.board[r][c+3] == self.player_turn:
                    return True

        # Check for vertical win
        for r in range(self.BOARD_ROWS-3):
            for c in range(self.BOARD_COLUMNS):
                if self.board[r][c] == self.player_turn and self.board[r+1][c] == self.player_turn and self.board[r+2][c] == self.player_turn and self.board[r+3][c] == self.player_turn:
                    return True

        # Check for positively sloped diagonal win
        for r in range(self.BOARD_ROWS-3):
            for c in range(self.BOARD_COLUMNS-3):
                if self.board[r][c] == self.player_turn and self.board[r+1][c+1] == self.player_turn and self.board[r+2][c+2] == self.player_turn and self.board[r+3][c+3] == self.player_turn:
                    return True

        # Check for negatively sloped diagonal win
        for r in range(3, self.BOARD_ROWS):
            for c in range(self.BOARD_COLUMNS-3):
                if self.board[r][c] == self.player_turn and self.board[r-1][c+1] == self.player_turn and self.board[r-2][c+2] == self.player_turn and self.board[r-3][c+3] == self.player_turn:
                    return True

        # Check if board is full - end in draw
        if 0 not in self.board[-1]:
            self.player_turn = 0
            return True

        return False