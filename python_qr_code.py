# To use this script, please follow the installation of a few python packages
# - use `pip install qrcode[pil]`

import qrcode

message = input("Please enter the info or link you want to make a qr code: ")


img = qrcode.make(message)

qr_name = input("Please enter the name of the QR Code you want to make: ")

type(img)  # qrcode.image.pil.PilImage

img.save(f"{qr_name}.png")
