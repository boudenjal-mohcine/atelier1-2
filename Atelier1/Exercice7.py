# ON VA LIRE LES CARACTERES DE CETTE CHANE EN INVERSE (PAS : -1)
def inverse(string):
  for i in range(len(string)-1,-1,-1):
   print(string[i],end='')
