# Importation des modules
import random

# Generation de l'adresse mac
choices = ["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

new_adress = ""

while len(new_adress) < 12 :
	new_adress += random.choice(choices)
	
print(new_adress)