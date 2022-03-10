'''rie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmo', 'Bahia', 'Sport Recife', 'Chapecoense')

print(f'OS CINCO PRIMEIROS COLOCADOS SÃO: {tabela[0:5]}')
print('=' * 100)
print(f'OS ÚLTIMOS QUATRO COLOCADOS SÃO: {tabela[-4:]}')
print('=' * 100)
print(f'TIMES PERFILADOS EM ORDEM ALFABÉTICA {sorted(tabela)}')
print('=' * 100)
print(f'O TIME DA {tabela[19]} ESTÁ EM {tabela.index(tabela[19])}ª POSIÇÃO NA TABELA.')
