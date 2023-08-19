# Importation des modules
import random
import psutil

# Generation de l'adresse mac
choices = ["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

new_adress = ""

while len(new_adress) < 12 :
	new_adress += random.choice(choices)
	
listKeys = list(psutil.net_if_addrs().keys())
cartes_réseau = ""

for elem in listKeys :
	cartes_réseau+="\n     "+str(listKeys.index(elem)+1)+". "+elem+"\n"
	

selection_card = input('Quelle carte réseau souhaitez-vous sélectionner ?\n'+ cartes_réseau +'\nEntrer son numéro :')

try:
    int(selection_card)
except ValueError:
    print("Ce n'est pas un nombre entier valide. Relancez le programme")
    
selected_card = listKeys[int(selection_card)-1]

infos_card = psutil.net_if_addrs()[selected_card][0][1]

print(infos_card)