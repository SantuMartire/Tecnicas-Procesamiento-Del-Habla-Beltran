from nltk import word_tokenize
# Texto que deseas tokenizar
text = "El verdadero peligro no es que las computadoras empiecen a pensar como hombres, sino que los hombres empiecen a pensar como computadoras. Sydney G. Harris"
text_tokenizado = word_tokenize(text)
print(text)
print(text_tokenizado)
print(len(text_tokenizado))
