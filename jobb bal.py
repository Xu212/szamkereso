numbers = [100847, 535942, 82760, 193097, 590573, 854689, 2254, 685232, 854781, 262321, 690067, 963085, 41075, 728201, 4707, 760822]
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

def jobb_bal_keres():
    for n in numbers:
        n_szov = str(n)
        hossz = len(n_szov)
        
        for sor_idx, sor in enumerate(matrix):
            sor_str = "".join(map(str, sor))
            
            if n_szov in sor_str:
                c_idx = sor_str.find(n_szov)
                print(f"Szám: {n} | Sor: {sor_idx}, Oszlop: {c_idx} (Balról -> Jobbra)")
                
            bal_sor = sor_str[::-1]
            if n_szov in bal_sor:
                rev_idx = bal_sor.find(n_szov)
                orig_c_idx = len(sor) - 1 - rev_idx
                print(f"Szám: {n} | Sor: {sor_idx}, Oszlop: {orig_c_idx} (Jobbról -> Balra)")

jobb_bal_keres()
