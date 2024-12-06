
from rich import print
from rich import traceback
import re
# load the rich stuff
traceback.install()

file_name = "input.txt"
total = 0


      
      
      
def check_h(list, row_index=None, debug=False):
    xmases = 0
    row_str = ''.join(list)
    
    # Check forward
    if 'XMAS' in row_str:
        forward_count = row_str.count('XMAS')
        xmases += forward_count
        if debug and forward_count > 0:
            print(f"Horizontal forward XMAS in {row_str}: {forward_count}")
    
    # Check backwards
    reverse_row_str = ''.join(list[::-1])
    if 'XMAS' in reverse_row_str:
        backward_count = reverse_row_str.count('XMAS')
        xmases += backward_count
        if debug and backward_count > 0:
            print(f"Horizontal backward XMAS in {reverse_row_str}: {backward_count}")
    
    return xmases

def check_v(grid, debug=False):
    xmases = 0
    columns = [
        [grid[row][col] for row in range(len(grid))]
        for col in range(len(grid[0]))
    ] 
    
    for column in columns:
        xmases += check_h(column, debug=debug)
    
    return xmases

def check_diagonals(grid):
    xmases = 0
    height = len(grid)
    width = len(grid[0])

    # Tracking to prevent double-counting
    unique_xmas_positions = set()

    # Top-left to bottom-right diagonals
    for start_row in range(height):
        for start_col in range(width):
            diagonal = []
            r, c = start_row, start_col
            while r < height and c < width:
                diagonal.append(grid[r][c])
                r += 1
                c += 1
                
                # Check diagonal if long enough
                if len(diagonal) >= 4:
                    diagonal_str = ''.join(diagonal)
                    
                    # Check forward
                    if 'XMAS' in diagonal_str:
                        for i in range(len(diagonal_str) - 3):
                            if diagonal_str[i:i+4] == 'XMAS':
                                # Use more precise unique position tracking
                                unique_pos = (start_row + i, start_col + i, 'TL-BR-forward')
                                if unique_pos not in unique_xmas_positions:
                                    xmases += 1
                                    unique_xmas_positions.add(unique_pos)
                    
                    # Check backwards
                    reverse_diagonal_str = ''.join(diagonal[::-1])
                    if 'XMAS' in reverse_diagonal_str:
                        for i in range(len(reverse_diagonal_str) - 3):
                            if reverse_diagonal_str[i:i+4] == 'XMAS':
                                # More precise position tracking
                                unique_pos = (start_row + len(diagonal) - 1 - i, 
                                              start_col + len(diagonal) - 1 - i, 
                                              'TL-BR-backward')
                                if unique_pos not in unique_xmas_positions:
                                    xmases += 1
                                    unique_xmas_positions.add(unique_pos)

    # Top-right to bottom-left diagonals
    for start_row in range(height):
        for start_col in range(width):
            diagonal = []
            r, c = start_row, start_col
            while r < height and c >= 0:
                diagonal.append(grid[r][c])
                r += 1
                c -= 1
                
                # Check diagonal if long enough
                if len(diagonal) >= 4:
                    diagonal_str = ''.join(diagonal)
                    
                    # Check forward
                    if 'XMAS' in diagonal_str:
                        for i in range(len(diagonal_str) - 3):
                            if diagonal_str[i:i+4] == 'XMAS':
                                unique_pos = (start_row + i, start_col - i, 'TR-BL-forward')
                                if unique_pos not in unique_xmas_positions:
                                    xmases += 1
                                    unique_xmas_positions.add(unique_pos)
                    
                    # Check backwards
                    reverse_diagonal_str = ''.join(diagonal[::-1])
                    if 'XMAS' in reverse_diagonal_str:
                        for i in range(len(reverse_diagonal_str) - 3):
                            if reverse_diagonal_str[i:i+4] == 'XMAS':
                                unique_pos = (start_row + len(diagonal) - 1 - i, 
                                              start_col - (len(diagonal) - 1 - i), 
                                              'TR-BL-backward')
                                if unique_pos not in unique_xmas_positions:
                                    xmases += 1
                                    unique_xmas_positions.add(unique_pos)

    return xmases

# Main execution
with open(file_name) as text:
    total = 0  # Initialize total
    grid = [list(row) for row in text.read().strip().split('\n')]
    
    # Horizontal check
    total += sum(check_h(line) for line in grid)
    
    # Vertical check
    total += check_v(grid)
    
    # Diagonal check
    total += check_diagonals(grid)
    
    print(f' final: {total}')
