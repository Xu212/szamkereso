numbers = [
    100847, 535942, 82760, 193097, 590573, 854689, 2254, 685232,
    854781, 262321, 690067, 963085, 41075, 728201, 4707, 760822
]


matrix = [
    [7, 9, 8, 6, 4, 5, 8, 0, 9, 8],
    [6, 6, 1, 3, 8, 6, 7, 9, 1, 6],
    [0, 1, 8, 7, 4, 5, 8, 0, 2, 1],
    [0, 4, 0, 6, 5, 3, 2, 8, 1, 2],
    [9, 6, 3, 1, 8, 5, 1, 3, 4, 4],
    [6, 6, 7, 8, 8, 9, 0, 5, 2, 7],
    [5, 5, 5, 2, 0, 4, 2, 3, 9, 0],
    [6, 1, 0, 2, 8, 2, 7, 6, 4, 1],
    [0, 4, 9, 5, 1, 9, 3, 0, 9, 7],
    [9, 9, 5, 4, 1, 3, 9, 3, 7, 4]
]
#jobbra le
"""def jobbra_le(matrix, numbers):
    sorok = len(matrix)
    oszlopok = len(matrix[0]) if sorok > 0 else 0
    
    for szamsor in numbers:
        szamsor_str = str(szamsor)
        hossz = len(str(szamsor))
        elso_szamjegy = int(szamsor_str[0])

        for sor in range(sorok):
            for oszlop in range(oszlopok):  

                if matrix[sor][oszlop] == elso_szamjegy:   
                    
                    if oszlop + hossz <= oszlopok and sor + hossz <= sorok:
    
                        for i in range(1, hossz): 

                            if matrix[sor + i][oszlop + i] == int(szamsor_str[i]):
                                
                                if i == hossz-1:
                                    print(f"{szamsor} megtalálva átlóba (átló - jobbra le). Pozija{sor+1}{oszlop+1} - vége {sor+1}") 
                                
                            else:

                                break   """
"""def le(matrix, numbers):
    sorok = len(matrix)
    oszlopok = len(matrix[0]) if sorok > 0 else 0
    
    for szamsor in numbers:
    #adott számsorozat kiválasztása
        szamsor_str = str(szamsor)
        hossz = len(str(szamsor))
        elso_szamjegy = int(szamsor_str[0])

        for sor in range(sorok):
            for oszlop in range(oszlopok):
            #számkeresés egyesével    

                if matrix[sor][oszlop] == elso_szamjegy:
                #ha egyezik    
                    
                    if sor + hossz <= sorok:
                    #ha kifér
                        #akkor a második elem vizsgálata következik
                        for i in range(1, hossz): #mivel az első elemet már vizsgáltuk

                            if matrix[sor + i][oszlop] == int(szamsor_str[i]):
                                
                                if i == hossz-1:
                                    print(f"{szamsor} megtalálva átlóba (le). Pozija{sor+1}{oszlop+1} - vége {sor+1}") 
                                
                            else:
                                break            
"""

def jobbra_fel(matrix, numbers):
    sorok = len(matrix)
    oszlopok = len(matrix[0]) if sorok > 0 else 0
    
    #adott számsorozat kiválasztása
    for szamsor in numbers:
        szamsor_str = str(szamsor)
        hossz = len(str(szamsor))
        elso_szamjegy = int(szamsor_str[0])

        for sor in range(sorok):
            for oszlop in range(oszlopok):
                #mátrix bejárása  
                
                if matrix[sor][oszlop] == elso_szamjegy:   
                    #első számjegy egyezik?

                    if sor - hossz + 1 >=0 and oszlop + hossz <= oszlopok:
                        #vizsgálat, hogy mátrixon belül marad-e
    
                        for i in range(1, hossz): 

                            if matrix[sor - i][oszlop + i] == int(szamsor_str[i]):
                                #egyezés
                                
                                if i == hossz-1:
                                    print(f"{szamsor} megtalálva átlóba (átló - jobbra fel). Pozija{sor+1}{oszlop+1}") 
                                
                            else:

                                break
def balra_le(matrix, numbers):
    sorok = len(matrix)
    oszlopok = len(matrix[0]) if sorok > 0 else 0
    
    for szamsor in numbers:
        szamsor_str = str(szamsor)
        hossz = len(str(szamsor))
        elso_szamjegy = int(szamsor_str[0])

        for sor in range(sorok):
            for oszlop in range(oszlopok):  
                
                if matrix[sor][oszlop] == elso_szamjegy:   
                    
                    if sor + hossz <= sorok and oszlop - hossz + 1 >= oszlopok:
    
                        for i in range(1, hossz): 

                            if matrix[sor + i][oszlop - i] == int(szamsor_str[i]):
                                
                                if i == hossz-1:
                                    print(f"{szamsor} megtalálva átlóba (átló - balra le). Pozija{sor+1} {oszlop+1}") 
                                
                            else:

                                break      

jobbra_fel(matrix,numbers)
balra_le(matrix,numbers)




