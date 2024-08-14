import math

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i*3], "|", board[i*3 + 1], "|", board[i*3 + 2], "|")
        print("-------------") 

def check_winner(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                      (0, 4, 8), (2, 4, 6)]             
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] and board[cond[0]] != ' ':
            return board[cond[0]]
    return None

def check_draw(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [' ' for _ in range(9)]
    print_board(board)
    
    while True:
        while True:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                board[move] = 'O'
                break
            else:
                print("Invalid move. Try again.")
        
        print_board(board)
        
        if check_winner(board):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        print("AI's turn:")
        move = best_move(board)
        board[move] = 'X'
        print_board(board)
        
        if check_winner(board):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

play_game()
