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


def lefelszamok(n):
    return [int(d) for d in str(n)]


def find_numbers_vertical(matrix, numbers):
    n = len(matrix)
    if n == 0:
        return []
    m = len(matrix[0])

    results = []

    for num in numbers:
        target = lefelszamok(num)
        tlen = len(target)
        found_any = False

        for c in range(m):
            for r in range(n):
                if r + tlen <= n:
                    ok = True
                    for k in range(tlen):
                        if matrix[r + k][c] != target[k]:
                            ok = False
                            break
                    if ok:
                        found_any = True
                        results.append((num, True, 'down', (r, c), (r + tlen - 1, c)))
                if r - tlen + 1 >= 0:
                    ok = True
                    for k in range(tlen):
                        if matrix[r - k][c] != target[k]:
                            ok = False
                            break
                    if ok:
                        found_any = True
                        results.append((num, True, 'up', (r, c), (r - tlen + 1, c)))

        if not found_any:
            results.append((num, False, None, None, None))

    return results


def print_vertical_findings(matrix, numbers):
    results = find_numbers_vertical(matrix, numbers)
    for num, found, direction, start, end in results:
        if found:
            print(f"{num}: talalt! {direction}, kezd: {start}, veg: {end}")
        else:
            print(f"{num}: nincs talalva")


if __name__ == '__main__':
    print('Numbers:', numbers)
    print('Matrix:')
    for sor in matrix:
        print(' '.join(str(x) for x in sor))

    print('\n-- eredmenyek --')
    print_vertical_findings(matrix, numbers)
