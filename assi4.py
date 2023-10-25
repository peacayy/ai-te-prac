#!/usr/bin/env python
# coding: utf-8

# In[1]:


#A68; assignment:4
def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row == len(board):
        return True
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0
    
    return False

def print_solution(board):
    for row in board:
        print(' '.join(['Q' if col == 1 else '.' for col in row]))

def n_queens(num):
    board = [[0 for _ in range(num)] for _ in range(num)]
    
    if not solve_n_queens(board, 0):
        print("No solution exists")
        return
    
    print_solution(board)

if __name__ == "__main__":
    n_queens(8)


# In[ ]:




