from itertools import count


class Letters:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'á', 'ã', 'é', 'ê', 'í', 'ó', 'ô', 'ú', 'ç', '!', '?', '.', ',', '-']

    def findLetterIndex(self, letter):
        return self.letters.index(letter)

    def getLetter(self, index):
        return self.letters[index]
    
    def getLength(self):
        return len(self.letters)
