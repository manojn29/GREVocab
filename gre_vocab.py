import json

class greVocab:

    def __init__(self):
        self.wordList = []
        self.alpha = {}
        self.data = {}

    def readJson(self):
        with open('words.json') as words:
            self.data = json.load(words)

            self.wordList = list(self.data['words'].keys())

            for i in range(97, 123):
                self.alpha[chr(i)] = []

            for word in self.wordList:
                self.alpha[word[0]].append(word)

    def getCount(self, letter):
        count = 0
        for letters in self.alpha:
            count += len(self.alpha[letters])
            if(letters == letter):
                break
        return count

    def getCountTill(self, iletter, jletter):
        count = 0
        for i in range(ord(iletter), ord(jletter)+1):
            count += len(self.alpha[chr(i)])
        return count

from gre_vocab import greVocab
o = greVocab()
o.readJson()
alpha = o.alpha
wordlist = o.wordList
print(o.getCountTill('j', 'z'))