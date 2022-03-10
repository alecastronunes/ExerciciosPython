import hashlib
texto = str(input('Digite a frase ou palavra que desja converter para md5: '))
#Converte a frase digitada para MD5.
converte = hashlib.md5(texto.encode())
#Transforma o MD5 em exadecimal.
resultado = converte.hexdigest()
print(resultado)
