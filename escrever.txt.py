with open('texto.txt', 'w') as arquivo:
    texto = list()

    texto.append("Esta é a primeira limda de texto.\n")
    texto.append("Aqui esta a segunda frase.\n")
    texto.append("E esta é a terceira frase do arquivo\n")

    arquivo.writelines(texto)

print("Arquivo 'texto.txt' criado e conteúdo gravado com sucesso")