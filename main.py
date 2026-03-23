import jobb_bal
import jobb_le
import lefelfelle
import Progal_L_Bence
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
print("Függőlegesen megtalált számok:")
lefelfelle.print_vertical_findings(matrix,numbers)
print("Vízszintesen megtalált számok :", end= "")
Progal_L_Bence.megoldas(matrix,numbers)
print("Átlósan felfelé megtalált számok: ",end="")
jobb_bal.jobb_bal_keres(matrix, numbers)
print("Átlósan lefelé megtalált számok: ", end="")
jobb_le.showResult(matrix, numbers)