

def jobb_bal_keres(matrix, numbers):
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
