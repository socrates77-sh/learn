# -*- coding: utf-8 -*-
"""
创建一个1000*1000的24bit的BMP图像。
"""
header = 'BM\xf6\xc6-\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\xc0\xc6-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
f = file("tmp.bmp", "wb")
f.write(header)
f.write("\x00"*(1000*1000*3))
f.close()
