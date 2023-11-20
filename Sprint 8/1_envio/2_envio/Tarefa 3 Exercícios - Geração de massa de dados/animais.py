animais = ["gato", "cachorro", "cobra", "jacaré", "peixe", "macaco", "urso", "leão", "camaleão",
           "elefante", "leopardo", "girafa", "baleia", "hipopótamo", "pássaro", "raposa", "rinoceronte", "tartaruga", "morcego"]


# Ordenar em ordem crescente
animais_ordenados = sorted(animais)

# Imprimir os animais um a um
print("\n".join(animais_ordenados))

# Armazenar em um arquivo CSV
import csv

with open('animais.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for animal in animais_ordenados:
        writer.writerow([animal])
