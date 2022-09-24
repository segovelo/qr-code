# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 14:19:12 2022

@author: Sebastian
"""

import qrcode

website_link = 'https://github.com/segovelo'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('segovelo_qr.png')