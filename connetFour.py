import random
class connect_four:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.players = 2
        self.board = self.build_board(self.rows, self.columns)
        self.empty = " "
        self.player_one_tile = "o"
        self.player_two_tile = "x"
        self.turn = "one"

    def build_board(self, rows, columns):
        board = []
        for row in range(rows):
            r = [" "]*columns
            board.append(r)
        return board

    def take_turns(self):
        taken = False
        r = [0,1,2,3,4,5]
        random.shuffle(r)
        if self.turn == 'one':
            for row in r:
                for column in range(len(self.board)-1, -1, -1):
                    if self.board[row][column] == " ":
                        self.board[row][column] = self.player_one_tile
                        taken = True
                        break;
                if taken == True:
                    break;
            self.turn = 'two'
        else:
            for row in r:
                for column in range(len(self.board)-1,-1,-1):
                    if self.board[row][column] == " ":
                        self.board[row][column] = self.player_two_tile
                        taken = True
                        break;
                if taken == True:
                    break;
            self.turn = 'one'
        if self.check_winner() == self.empty:
            if self.check_full() == True:
                return 'draw'
            else:
                return self.take_turns()
        elif self.check_winner() == self.player_one_tile:
            return 'player_one_wins'
        else:
            return 'player_two_wins'

    def check_full(self):
        for i in range(len(self.board)):
            if self.empty in self.board[i]:
                return False
        return True

    def check_winner(self):
        for i in self.board:
            print('\t'.join(map(str, i)))
        print('--------------------------------')
        for i in range(self.rows):
            for j in range(self.columns):
                if j+3 < self.columns and self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] and self.board[i][j] != self.empty:
                    return self.board[i][j]
                if i+3 < self.rows and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] and self.board[i][j] != self.empty:
                    return self.board[i][j]
                if i+3 < self.rows and j+3 < self.columns and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] and self.board[i][j] != self.empty:
                    return self.board[i][j]
                if i-3 >= 0 and j-3 >= 0 and self.board[i][j] == self.board[i-1][j-1] == self.board[i-2][j-2] == self.board[i-3][j-3] and self.board[i][j] != self.empty:
                    return self.board[i][j]
        return self.empty


game = connect_four()
print(game.take_turns())