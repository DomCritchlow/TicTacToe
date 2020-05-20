class Board():
    
    def __init__(self, n, boarder = "#"):
        
        self.boarder = boarder
        self.board_size = n
        self.board = [["-" for x in range(n)] for y in range(n)]
        
        return
    
    def place(self, value, row, col, show = False):
        
        if row >= self.board_size or row<0:
            return False
        
        if col >= self.board_size or col<0:
            return False
        
        if self.board[row][col] == "-":
            self.board[row][col] = value
        else :
            return False
        
        if show:
            print(self.__str__())
            
        return True
        
    def __str__(self):
        
        t = '   '
        bar = "  "+ ''.join((2+self.board_size)*[self.boarder + " "])
        col = ''.join([' ' + str(i) for i in range(self.board_size)]) 
        
        t += col + "\n"
        t += bar + "\n"

        for i in range(self.board_size):
            t += str(i) + " " +(self.pline(self.board[i])) +"\n"
            
        t += bar + "\n"
        
        return t
    
    def pline(self, row):
        
        m_str = self.boarder 
        for i in range(self.board_size):
            m_str += " " + str(row[i])
            
        m_str += (" " + self.boarder )
        
        return m_str
    
    def __repr__(self):
        
        return self.__str__()

    
class Game():
    
    def __init__(self, n, first ='X', boarder = "#"):
        
        self.Board = Board(n, boarder)
        self.player = first
        self.move_count = 0
        self.gameover = False
        self.tie = False
        self.iswinner = False
        
    def move(self, row, col, show = False):
        
        if self.Board.place(self.player, row, col, show):
            self.move_count += 1
            
            self.checkwinner(row, col)
            if self.gameover:
                return True
            
            self.next_player()
            
        else:
            if show:
                print(self.Board)
            print("Not a valid position! " + self.player +" pick a different spot")
            return False
        print ("Player " + self.player + " Turn")
        
        return True
    
    def next_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
    
    def checkwinner(self, row, col):
        
        if self.move_count == self.Board.board_size * self.Board.board_size:
            print("TIED!")
            self.tie = True
            self.gameover = True
            return
        
        #check row
        r_count = 0
        for i in range(self.Board.board_size):
            if self.Board.board[row][i] == self.player:
                r_count +=1
        if r_count == self.Board.board_size:
            self.win()
            return 
        
        
        #check col
        col_count = 0
        for i in range(self.Board.board_size):
            if self.Board.board[i][col] == self.player:
                col_count +=1
        if col_count == self.Board.board_size:
            self.win()
            return 
        
        
        #check diag 1
        diag_count = 0
        for i in range(self.Board.board_size):
            if self.Board.board[i][i] == self.player:
                diag_count +=1
        
        if diag_count == self.Board.board_size:
            self.win()
            return 
        
    
        #check diag 2
        diag2_count = 0
        for i in range(self.Board.board_size):
            if self.Board.board[i][self.Board.board_size-i-1] == self.player:
                diag2_count +=1
        if diag2_count == self.Board.board_size:
            self.win()
            return 
        
        return 
    
    def win(self):
        self.iswinner = True
        self.gameover = True
        print("Player " + self.player + " wins!")
        
    def show(self):
        print('\n')
        print(self.Board)
        
    def __str__(self):
        
        m_str = "Current Player: " + self.player + "\n"
        
        m_str += "Positions played: " + str(self.move_count) + "\n"
        
        m_str += "Open spots: " + str(self.Board.board_size*self.Board.board_size - self.move_count) + "\n\n"
        
        m_str += "Current Game Board\n" + str(self.Board)
        
        if self.tie:
            m_str += "\n\n" + "The Game is over and it is Tied \n"
        elif self.gameover:
            m_str += "\n\n" + "The Game is over and player " + self.player + " has won!\n" 
        
        return m_str
    
    def isgameover(self):
        return self.gameover
    
    def winner(self):
        if not self.gameover and not self.tie:
            return False
        return self.player
    
    def istie(self):
        return self.tie
    
    def __repr__(self):
        
        return self.__str__()