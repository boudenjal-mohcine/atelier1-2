# Fonction qui fait la somme du certain a on arrivant au 0 (a+(a-1)+(a-2)....)
# On va faire appelle au meme fonction avec un désincrimentation du a
def som(a) :
 if a>0 :
   return a+som(a-1)
 else :
   return a

# L'utiisateur va choisir un nombre pour calculer la somme de ce nombre jusqu'à 1
n = int(input("Entrer un nombre : "))
print("la somme de 1 jusqu'à",n,"est :",som(n))
