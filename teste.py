''''c = 1
numero = int(input('Quer contar até quanto?'))
while c < numero+1:
    print(c)
    c = c + 1
print('FIM')'''

'''
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} número pares e {} números ímpares!'.format(par, impar))
'''
'''#ocultar senha do usuário.
from getpass import getpass
usarname = str(input('Enter Username: '))
password = getpass('Enter password: ')

print(f'Seu usuário é: {usarname} e sua senha é: {password}')'''

#Tuplas
#lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
#1° forma de fazer o FOR
#for c in lanche:
    #print(f'Eu vou comer {c}')

#2° forma de fazer o FOR
#for cont in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]}')
    #print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#3° forma de fazer o FOR
#for posicao, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida}, na posição {posicao}')
'''import youtube_dl
def run():
    video_url = input("please enter youtube video url:")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__=='__main__':
    run()'''

precos = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)
print(f'O indix é: {precos.index(1.75)}')