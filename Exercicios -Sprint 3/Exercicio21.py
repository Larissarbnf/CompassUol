class Passaro: #Criando a classe pato
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        pass


class Pato(Passaro): 
    def emitir_som(self):
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        print("Piu Piu")


# Testando as classes
pato = Pato()
print("Pato")
pato.voar()
print("Pato emitindo som...")
pato.emitir_som()

print()

pardal = Pardal()
print("Pardal")
pardal.voar()
print("Pardal emitindo som...")
pardal.emitir_som()
