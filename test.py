                       #TABLE DE MULTIPLICATION

print("Vous voulez connaître la table de multiplication d'un nombre compris entre 0 et 10 ? ")
val = int(input("Saississez le nombre svp : "))
print("La table de multiplication de ",val)

for i in range(0, 11) :
    print (i, " * ", val, "=", i*val)
    i+=1
