# Fonction pour calculer le factorielle d'un nombre :
def fact(a):
 if (a!=0) :
   return a*fact(a-1);
 else:
    return 1 ;

# Calculer la somme de 1!/1 + 2!/2 + 3!/3 + 4!/4 + 5!/5 :
# Remarquant que si par exemple on a 4!/4 = 4x3x2x1/4 on peut simpilifier par 4 on obient 3x2x1 c-à-d 3! :

print("Programme qui calcule la somme d'une serie sous forme de (n=5): 1!/1 + 2!/2 + 3!/3 + 4!/4 + 5!/5 =",(fact(4)+fact(3)+fact(2)+fact(1)+1))

# Calcule d'un N choisi par l'utilisateur : 

n = int(input("Entrer un nombre : "))
somme = 1
i=1

for i in range(n,1,-1):
  somme=somme+fact(i-1)

print("la somme est : ",somme)    
