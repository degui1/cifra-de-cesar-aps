def verificarIndexador(numero):
    while (numero > 25):
        numero -= 26

    return numero


class CifraCesar:
    def __init__(self, num, letters):
        if (num < 0):
            num += 26

        self.indexer = verificarIndexador(num)
        self.letters = letters
        self.message = ''

    def encriptarMensagem(self, text):
        str(text).split()
        for letter in text:
            try:
                index = self.letters.findLetterIndex(letter)
                self.message += self.letters.getLetter(
                    verificarIndexador(index + self.indexer))
            except:
                self.message += letter
        else:
            return self.message
