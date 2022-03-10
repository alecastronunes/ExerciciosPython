import easyocr

#Define o idioma
idioma = easyocr.Reader(['pt'])

#Extrai o texto da imagem
imagem = idioma.readtext('conteudo.png', paragraph = True)

#Para cada resultado de texto na imagem, imprime uma linha.
for resultado in imagem:
    print('Texto encontrado: {}'.format(resultado[1]))
        #f'\t Posição: {resultado[0]}\n'
        #f'\tTexto: {resultado[1]}\n')
