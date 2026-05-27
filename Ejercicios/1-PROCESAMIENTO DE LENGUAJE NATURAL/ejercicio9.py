import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpus = PlaintextCorpusReader(".", 'melville-moby_dick.txt')

ocurrencies=corpus.words()
tipus=set(ocurrencies)

print("OCURRENCIAS:",len(ocurrencies))
print("TIPOS:",len(tipus))