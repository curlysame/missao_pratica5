txt = open('loremipsum.txt', 'r')

conteudo = txt.read()

#print("Inprima na tela todo o conteudo")
#print(conteudo)

#print("Imprima na tela os primeiros caracteres: ")
#print(conteudo[:3])

with open('loremipsum.txt', 'r') as txt:
    conteudo = txt.read()

print(conteudo)    