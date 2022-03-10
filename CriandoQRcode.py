import qrcode
#Endereço de apontamento no qrcode.
url = 'https://www.uol.com.br/'

#Cria o objeto do qrcode.
qr = qrcode.QRCode(version = 1, box_size = 4, border = 5)
qr.add_data(url)
qr.make(fit = True)

#Cria a imagem do qrcode.
img = qr.make_image(fill = 'black', back_color = 'white')
img.show()
