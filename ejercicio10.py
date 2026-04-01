import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpus = PlaintextCorpusReader(".", 'melville-moby_dick.txt')

ocurrencies=corpus.words()
tipus=set(ocurrencies)
riquezalexica=len(ocurrencies)/len(tipus)

print("OCURRENCIAS:",len(ocurrencies))
print("TIPUS:",len(tipus))
print("RIQUEZA LÊXICA:",round(riquezalexica,2))