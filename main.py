from colorama import init
init()

numbers = [
    100847, 535942, 82760, 193097, 590573, 854689, 2254, 685232,
    854781, 262321, 690067, 963085, 41075, 728201, 4707, 760822
]

matrix = [
    [7, 9, 8, 6, 4, 5, 8, 0, 9, 8],
    [6, 6, 1, 3, 8, 6, 7, 9, 1, 6],
    [0, 1, 8, 7, 4, 5, 8, 0, 2, 1],
    [0, 4, 0, 6, 5, 3, 2, 8, 1, 2],
    [9, 6, 3, 0, 8, 5, 1, 3, 6, 4],
    [6, 6, 7, 8, 8, 9, 0, 2, 2, 7],
    [5, 5, 5, 2, 0, 4, 3, 3, 9, 0],
    [6, 1, 0, 2, 8, 2, 7, 6, 4, 1],
    [0, 4, 9, 5, 1, 9, 3, 0, 9, 7],
    [9, 9, 5, 4, 1, 3, 9, 3, 7, 4]
]

def jobble(matrix, numbers):
    rows = len(matrix)
    cols = len(matrix[0])

    directions = [(1,1), (-1,-1)]
    results = []
    highlight = set()

    for number in numbers:
        digits = list(map(int, str(number)))
        found_positions = []

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] != digits[0]:
                    continue

                for dr, dc in directions:
                    path = [(r, c)]
                    nr, nc = r, c
                    i = 1

                    while i < len(digits):
                        nr += dr
                        nc += dc

                        if not (0 <= nr < rows and 0 <= nc < cols):
                            break

                        if matrix[nr][nc] != digits[i]:
                            break

                        path.append((nr, nc))
                        i += 1

                    if i == len(digits):
                        found_positions.append(path)
                        highlight.update(path)

        results.append(found_positions)

    return results, highlight


results, highlight = jobble(matrix, numbers)
print("Találatok:")
for i, res in enumerate(results):
    if res:
        print(f"{numbers[i]} -> {res}")
print("\nSzínezett mátrix:")

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if (r, c) in highlight:
            print(f"\033[42m{matrix[r][c]}\033[0m", end=" ")
        else:
            print(matrix[r][c], end=" ")
    print()