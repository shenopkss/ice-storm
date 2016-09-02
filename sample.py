#!/usr/bin/env python
# encoding: utf-8
from PIL import Image
from PIL import ImageGrab
import hashlib
import time

def vertical_split(im3):
    inletter = False
    foundletter=False
    start = 0
    end = 0

    letters = []

    for y in range(im3.size[0]):
        for x in range(im3.size[1]):
            pix = im3.getpixel((y,x))
            if pix != 255:
                inletter = True
        if foundletter == False and inletter == True:
            foundletter = True
            start = y

        if foundletter == True and inletter == False:
            foundletter = False
            end = y
            letters.append((start,end))

        inletter=False

    count = 0
    result = []
    for letter in letters:
        m = hashlib.md5()
        im4 = im3.crop(( letter[0] , 0, letter[1],im3.size[1] ))
        m.update("%s%s"%(time.time(),count))
        f= "./temp/%d.gif"%(count)
        im4.save(f)
        result.append(f)

        count += 1
    return result

def split(im):
    #  im = Image.open(oim)
    im2 = Image.new("P",im.size,255)

    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y,x))
            if pix[0] >= 210 and pix[1] >= 210 and pix[2] <= 70:
                im2.putpixel((y,x),0)

    #  im2.show()

    inletter = False
    foundletter=False
    start = 0
    end = 0

    letters = []

    for y in range(im2.size[1]):
        for x in range(im2.size[0]):
            pix = im2.getpixel((x,y))
            if pix != 255:
                inletter = True
        if foundletter == False and inletter == True:
            foundletter = True
            start = y

        if foundletter == True and inletter == False:
            foundletter = False
            end = y
            letters.append((start,end))

        inletter=False

    count = 0
    result = []
    for letter in letters:
        im3 = im2.crop(( 0, letter[0] , im2.size[0], letter[1]))
        im3.save("./origin/" + str(count) + ".gif")
        count += 1
        result = vertical_split(im3)
    return result

immm = Image.open("6.jpg")
split(immm)
