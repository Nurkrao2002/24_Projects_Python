import pyqrcode 
from pyqrcode import QRCode
import png
s = "https://github.com/"
url = pyqrcode.create(s) 
# url.svg('josh_QR_Code.svg',scale=2)
url.show("josh.png", scale = 5) 

