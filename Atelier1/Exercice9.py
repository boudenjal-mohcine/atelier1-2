def couple(mat,elem):  # FONCTION QUI RENVOIE LE COUPLE D'UN ELEMENT (elem) DANS UNE MATRICE (mat)
 for i in range(0,len(mat)): # BOUCLE DE PARCOURIR EN LIGNE
    for j in range(0,len(mat[0])): # BOUCLE DE PARCOURIR EN COLONNE
      if mat[i][j]==elem :     # VERIFIER L'ELEMENT 
        print("(",i,",",j,")")    # RENVOYER LE COUPLE i,j
# NOTANT QUE L'INDICE COMMENCE PAR 0


