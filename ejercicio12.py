import nltk

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import FreqDist
corpus = PlaintextCorpusReader(".", 'melville-moby_dick.txt')
print("Frecuencia absoluta \t frecuencia relativa \t palabra ")
frecuencia=FreqDist(corpus.words())

#[["PALABRA",22], ["OTRA", 12]]

for mc in frecuencia.most_common(25):
    palabra=mc[0]
    frecuencia_absoluta=mc[1]
    frecuencia_relativa=frecuencia.freq(palabra)
    cadena=str(frecuencia_absoluta)+"\t \t \t"+str(frecuencia_relativa)+"\t"+palabra
    
    print(cadena)