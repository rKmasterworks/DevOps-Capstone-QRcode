import segno

qrcode = segno.make_qr("Tom Cruise", mode="byte")
qrcode.save("DYNAMSOFT.png", scale=7)