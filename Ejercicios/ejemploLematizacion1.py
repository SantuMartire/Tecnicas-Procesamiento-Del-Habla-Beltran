import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("stripes", 'v')) #Verbo/verb Rayar o remover
print(lemmatizer.lemmatize("stripes", 'n')) #Sustantivo/noun Raya o Tira