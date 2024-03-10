import pyqrcode
import os.path

save_path = "c:/desktop/python/img_svg/"
info = input("Please paste the url: ")
qr_code_name = input("please type the name of of qr code: ")

url = pyqrcode.create(info)

#save qr code
url.svg(save_path + qr_code_name+".svg", scale=8)


# import pyqrcode
# url = pyqrcode.create('http://uca.edu')
# url.svg('uca-url.svg', scale=8)
# url.eps('uca-url.eps', scale=5)
# print(url.terminal(quiet_zone=1))