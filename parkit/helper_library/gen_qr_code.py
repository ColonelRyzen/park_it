import pyqrcode

# Generates a QR code png image based on the VIN number of the vehicle that is registered.
def gen_qr_code(vin_number):
    qr_image = pyqrcode.create(vin_number, error='L'm version=27, mode='binary')
    qr_image.png((vin_number + ".png"), scale=6, module_color=[0,0,0,128], background=[0xff, 0xff, 0xcc])
