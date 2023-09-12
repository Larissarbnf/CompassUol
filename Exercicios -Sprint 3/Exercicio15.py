class Lampada: #A classe Lampada possui um construtor __init__ que recebe um booleano determinando se a lâmpada está ligada ou desligada.
    def __init__(self, ligada=False):
        self.ligada = ligada

    def liga(self): # muda o estado da lâmpada para ligada
        self.ligada = True

    def desliga(self): #muda o estado da lâmpada para desligada
        self.ligada = False

    def esta_ligada(self): #retorna verdadeiro se a lâmpada está ligada 
        return self.ligada

# Teste da classe
lampada = Lampada()

# Ligue a lâmpada
lampada.liga()

# Imprima: A lâmpada está ligada? True
print("A lâmpada está ligada?", lampada.esta_ligada())

# Desligue a lâmpada
lampada.desliga()

# Imprima: A lâmpada ainda está ligada? False
print("A lâmpada ainda está ligada?", lampada.esta_ligada())