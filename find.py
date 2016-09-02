#!/usr/bin/env python
# encoding: utf-8


import glob
import os
import sys

from PIL import Image

EXTS = 'jpg', 'jpeg', 'JPG', 'JPEG', 'gif', 'GIF', 'png', 'PNG'


oim = Image.open('test.gif')
os.chdir('./dic')
images = []
for ext in EXTS:
    images.extend(glob.glob('*.%s' % ext))
for img in images:
    im = Image.open(img)
