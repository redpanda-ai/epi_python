def n_queens(n):
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result.append(list(col_placement))
            return
        for col in range(n):
            # Test if a newly placed queen will conflict any earlier queens
            # placed before.
            y = col_placement[:row]
            x = enumerate(y)

            for i, c in x:
                print(i, c)

            x = enumerate(col_placement[:row])

            if all(abs(c - col) not in (0, row - i)
                   for i, c in x):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result, col_placement = [], [0] * n
    solve_n_queens(0)
    return result

def to_text_representation(col_placement):
    sol = []
    for row in col_placement:
        line = ['\u25a1 '] * len(col_placement)
        line[row] = '\u25a0 '
        sol.append(''.join(line))
    return sol

result = n_queens(4)
for vec in result:
    text_rep = to_text_representation(vec)
    print(*text_rep, sep='\n')
    print()
