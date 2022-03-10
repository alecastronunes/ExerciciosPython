nome = 'Alexandre'
paletaCores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'vermelho': '\033[31m',
    'pretoebranco': '/033[7;39m'
}
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(paletaCores['vermelho'], nome , paletaCores['limpa']))