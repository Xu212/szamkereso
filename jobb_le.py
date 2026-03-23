def jobble(matrix, numbers):
    rows = len(matrix)
    cols = len(matrix[0])

    directions = [(1,1), (-1,-1)]
    results = []

    for number in numbers:
        digits = list(map(int, str(number)))
        found_positions = []

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] != digits[0]:
                    continue

                for directionRow, directionColumn in directions:
                    path = [(r, c)]
                    nextRow, nextColumn = r, c
                    i = 1

                    while i < len(digits):
                        nextRow += directionRow
                        nextColumn += directionColumn

                        if not (0 <= nextRow < rows and 0 <= nextColumn < cols):
                            break

                        if matrix[nextRow][nextColumn] != digits[i]:
                            break

                        path.append((nextRow, nextColumn))
                        i += 1

                    if i == len(digits):
                        direction = "↘" if (directionRow, directionColumn) == (1,1) else "↖"
                        found_positions.append((r, c, direction))

        results.append(found_positions)

    return results


def showResult(matrix, numbers):
    results = jobble(matrix, numbers)

    for i, res in enumerate(results):
        if res:
            print(f"{numbers[i]}:")
            for r, c, d in res:
                print(f"  sor: {r+1}, oszlop: {c+1}, irány: {d}")
        else:
            print(f"{numbers[i]}: nincs találat")