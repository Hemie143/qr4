import itertools

grid_static = [[1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 1, 1, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 0, 1, 1, 1, 0, 1],
               [1, 0, 1, 1, 1, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 0, 1, 1, 1, 0, 1],
               [1, 0, 1, 1, 1, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 0, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
               [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 2],
               [1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 2],
               [1, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 2],
               [1, 0, 1, 1, 1, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2],
               [1, 0, 1, 1, 1, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [1, 0, 1, 1, 1, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [1, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               ]

rule_hor_black = [19, 6, 14, 15, 15, 8, 19, 3, 13, 11, 16, 7, 16, 10, 9, 10, 16, 8, 16, 8, 16, 17, 13, 8, 20]
rule_hor_blocks = [5, 5, 8, 9, 8, 8, 7, 3, 7, 6, 7, 6, 9, 8, 8, 7, 6, 5, 7, 7, 7, 9, 8, 7, 6]
rule_ver_white = [5, 16, 13, 10, 9, 18, 6, 20, 9, 14, 18, 15, 7, 16, 13, 15, 14, 16, 9, 15, 8, 11, 13, 12, 10]

grid_size = 25

grid = [[0 for i in range(grid_size)] for j in range(grid_size)]


def row_count_blocks(row):
    grouped_row = [(k, sum(1 for i in g)) for k, g in itertools.groupby(row)]
    result = sum([1 for s in grouped_row  if s[0] == 2])
    return result

def generate_row(grid_ref, blacks_total, blocks_total):
    grid_ref_blacks = grid_ref.count(2)
    blacks to place = blacks_total - grid_ref_blacks
    return


def check_col(col):
    pass


while True:
    for row_num in range(grid_size):
        # Does not iterate through all combinations yet
        grid[row_num] = generate_row(grid_static, row_num, rule_hor_black[row_num], rule_hor_blocks[row_num])

    if all(check_col(col_num) for col_num in range(grid_size)):
        print('Found')
        print(grid)
        break

