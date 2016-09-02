#coding=utf-8

import os
from PIL import Image
from PIL import ImageGrab
from pymouse import PyMouse
import time
import math
import random
import win32api
import win32con
import split
import imghash
m = PyMouse()
sleeptime_count = 0
img = None
def find_question():
    if True:
        im = Image.open("./img/test6.jpg")
        #im = im2.convert("RGB")
        result = split.split(im)
        index = 0
        length = 0
        for item in result:
            print index
            im = Image.open(item)
            im_len = im.size[0] + 26
            length += im_len
            if imghash.match(item, 'dic') == True:
                length -= im_len / 2
                break
            index += 1
            print "\n"
        print "length:%d"%length
        exit()


if __name__=="__main__":
    find_question()
