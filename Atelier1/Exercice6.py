# TRI A BULLE :

def TRIABULLE(t,n):  # INVERSER CHAQUE 2 ELEMENTS SUCCESSIVE
  permut = True
  while (permut==True):
    permut = False    # ON VA QUITTER LA FONCTION SI ON A PAS ENCORE DE PERMITATION
    for j in range(0,n-1):
     if (t[j] > t[j+1]) :   # LE TRI DANS CE CAS FAIT D'UNE MANIERE CROISSANTE
      tmp = t[j+1]
      t[j+1] = t[j]       # tmp EST UN VARIABLE DANS LEQUEL ON VA CHANGER LE CONTENUE DE CHAQUE COUPLE SUCCESSIVE
      t[j] = tmp
      permut = True


# TRI PAR SELECTION : 

def TRISELECTION(t,n): #reduire le tableu pour chaque min ou max trouver (min pour cet exemple)
  for i in range(0,n-1):
   min = i
   for j in range(i+1,n): # chercher le min
    if(t[j] < t[min]):
     min = j
     if(min != i):  # permuter si ce min et plus petit que le premier
      tmp = t[i]
      t[i] = t[min]
      t[min] = tmp


# TRI PAR INSERTION :


def TRIINSERTION(t,n):  # INSERER CHAQUE ELEMENT ET TROUVER SA PLACE
  for i in range(1,n):
     k = t[i]   # CHAQUE ELEMENT INSERE DOIT ETRE COMPARER PAR TOUT LES AUTRES PRECEDENTS
     j=i
     while(j > 0 and t[j - 1] > k): 
       t[j] = t[j - 1]   # TROUVER LA BONNE PLACE ET PERMUTER 
       j=j-1
     t[j] = k
 
