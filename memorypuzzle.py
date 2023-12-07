import random

def create_board(size):
    characters = [chr(i) for i in range(65, 65 + size // 2)] * 2
    random.shuffle(characters)
    return [characters[i:i + int(size**0.5)] for i in range(0, size, int(size**0.5))]

def print_board(board, revealed):
    for i, row in enumerate(board):
        row_display = ''
        for j, cell in enumerate(row):
            row_display += cell if revealed[i][j] else '*'
            row_display += ' '
        print(row_display)

def memory_puzzle(size=16):
    board = create_board(size)
    revealed = [[False] * int(size**0.5) for _ in range(int(size**0.5))]
    remaining_pairs = size // 2

    while remaining_pairs > 0:
        print_board(board, revealed)
        print("Enter two tile coordinates to reveal (e.g., 0 1 0 2 for row 0 col 1 and row 0 col 2):")
        x1, y1, x2, y2 = map(int, input().split())

        if board[x1][y1] == board[x2][y2]:
            revealed[x1][y1] = revealed[x2][y2] = True
            remaining_pairs -= 1
            print("Match found!")
        else:
            print("Not a match. Try again.")
            print_board(board, revealed)

    print("Congratulations! You've found all pairs.")

memory_puzzle()
