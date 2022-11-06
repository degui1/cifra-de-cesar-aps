class Letters:
    def __init__(self):
        self.letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def encontrarLetra(self, letra):
        return self.letras.index(letra)

    def pegarLetra(self, indice):
        return self.letras[indice]
