from modules.letters import Letters

letters = Letters()

def verifyIndexer(number):
    while (number > letters.getLength() - 1):
        number -= letters.getLength()

    return number


class CifraCesar:
    def __init__(self, num):
        if (num < 0):
            num += letters.getLength()

        self.indexer = verifyIndexer(num)
        self.letters = letters
        self.message = ''

    def encryptMessage(self, text):
        self.message = ''
        str(text).split()
        for letter in text:
            try:
                index = self.letters.findLetterIndex(letter)
                self.message += self.letters.getLetter(
                    verifyIndexer(index + self.indexer))
            except:
                self.message += letter
        else:
            return self.message

    def decryptMessage(self):
        self.indexer *= -1
        self.encryptMessage(self.getMessage())
        self.indexer *= -1

    def getMessage(self):
        return self.message
