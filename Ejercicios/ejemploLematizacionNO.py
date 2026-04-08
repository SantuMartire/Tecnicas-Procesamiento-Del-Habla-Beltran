import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
#nltk.download('wordnet') #por unica vez

lemmatizer = WordNetLemmatizer()
# Definir la oración a lemmatizar
oracion = "The striped bats are hanging on their feet for best"
#Los murciélagos rayados están colgados de sus pies para estar mejor.
# Tokenizar la oración en palabras
word_list = nltk.word_tokenize(oracion)
print(word_list)
#> ['The', 'striped', 'bats', 'are', 'hanging', 'on', 'their', 'feet', 'for', 'best']

#Lemmatización de las palabras
for w in word_list:
    lemmatizer.lemmatize(w)
    print(w)
