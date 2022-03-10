from tqdm import tqdm

#for i in tqdm(range(10)):
    #time.sleep(1)

import requests
link = 'https://cep.awesomeapi.com.br/json/05424020'
'''
requisicao = requests.get(link)
resposta = requisicao.json()
cidade = resposta['city']
bairro = resposta['district']
print(f'A cidade é: {cidade} e o bairro é: {bairro}')'''

enderecos_entrega = []
# Pegar a lista de ceps
with open('ceps.txt', 'r') as arquivo:
    ceps = arquivo.read()
ceps = ceps.split('\n')
#print(ceps)

# Pegar a informação de cada CEP
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/05424020{cep}'
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
    if cidade == 'Rio de Janeiro':
        enderecos_entrega.append((cep, bairro))
print(f'Os endereços de entrega serão: {enderecos_entrega}')

