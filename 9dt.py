turn = 1
game = True
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
moves = []

if __name__ == "__main__":
    while game:
        # PROMPT USER FOR INPUT
        move = raw_input('> ')
        # EXIT GAME
        if move == 'EXIT':
            game = False
        # PRINT BOARD
        elif move == 'BOARD':
            print '|', board[0][3], board[1][3], board[2][3], board[3][3]
            print '|', board[0][2], board[1][2], board[2][2], board[3][2]
            print '|', board[0][1], board[1][1], board[2][1], board[3][1]
            print '|', board[0][0], board[1][0], board[2][0], board[3][0]
            print '+--------'
            print 'C 1 2 3 4'
        # GET MOVES
        elif move == 'GET':
            for move in moves:
                print move
        # PUT PIECE ON BAORD
        elif move[:3] == 'PUT':
            error = True
            # PLAYER 1 MADE VALID MOVE
            if turn % 2 == 1 and len(move) == 5 and move[4] in ['1','2','3','4']:
                win = [1,1,1,1]
                # CHECK IF ROW IS FULL - IF NOT UPDATE
                for i in range(4):
                    if board[int(move[4])-1][i] == 0:
                        board[int(move[4])-1][i] = 1
                        moves.append(move[4])
                        turn += 1
                        error = False
                        # CHECK WIN CONDITION
                        if board[0] == win or board[1] == win or board[2] == win or board[3] == win or board[:][0] == win or board[:][1] == win or board[:][2] == win or board[:][3] == win or [board[0][0], board[1][1], board[2][2], board[3][3]] == win or [board[0][3], board[1][2], board[2][1], board[3][0]] == win:
                            print 'WIN'
                            game = False
                        else:
                            print 'OK'
                        break
            # PLAYER 2 MADE VALID MOVE
            elif turn % 2 == 0 and len(move) == 5 and move[4] in ['1','2','3','4']:
                win = [2,2,2,2]
                # CHECK IF ROW IS FULL - IF NOT UPDATE
                for i in range(4):
                    if board[int(move[4])-1][i] == 0:
                        board[int(move[4])-1][i] = 2
                        moves.append(move[4])
                        turn += 1
                        error = False
                        # CHECK WIN CONDITION
                        if board[0] == win or board[1] == win or board[2] == win or board[3] == win or board[:][0] == win or board[:][1] == win or board[:][2] == win or board[:][3] == win or [board[0][0], board[1][1], board[2][2], board[3][3]] == win or [board[0][3], board[1][2], board[2][1], board[3][0]] == win:
                            print 'WIN'
                            game = False
                        else:
                            print 'OK'
                        break
            # PLAYER MADE INVALID MOVE
            if error:
                print 'ERROR'
        # BOARD FULL AND DRAW
        if 0 not in board[0] and 0 not in board[1] and 0 not in board[2] and 0 not in board[3]:
            print 'DRAW'
            game = False
