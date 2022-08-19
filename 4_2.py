frase = input('')
print(dict((i, frase.count(i)) for i in set(frase)))
