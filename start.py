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

m = PyMouse()
sleeptime_count = 0
img = None


def find_monsters():
    img = ImageGrab.grab((0, 0, 800, 622))
    # img = Image.open("test.jpg")
    size = img.size

    points = []
    monsters = []
    for j in xrange(0, size[1], 1):
        if j >= 380:
            break
        points = []
        i = 0
        while i < size[0]:
            if i >= 710 and j >= 340:
                break

            point = img.getpixel((i, j))
            point2 = img.getpixel((i, j + 1))
            # point3 = img.getpixel((i, j + 2))

            offset = 50
            offset2 = 10
            offset3 = 10
            # if abs(0 - point[0]) <= offset and abs(0 - point[1]) <= offset and abs(0 - point[2]) <= offset and abs(255 - point2[0]) <= offset2 and abs(0 - point2[1]) <= offset2 and abs(0 - point2[2]) <= offset2 and abs(156 - point3[0]) <= offset3 and abs(0 - point3[1]) <= offset3 and abs(0 - point3[2]) <= offset3:
            if abs(0 - point[0]) <= offset and abs(0 - point[1]) <= offset and abs(0 - point[2]) <= offset and abs(255 - point2[0]) <= offset2 and abs(0 - point2[1]) <= offset2 and abs(0 - point2[2]) <= offset2 :
                points.append([i, j])
            if len(points) > 0:
                monsters.append(points[0])
                i = points[0][0] + 32
                points = []
            else:
                i = i + 1
    return monsters

def kill(p):
    x = p[0] + 14
    y = p[1] + 55
    m.click(x,y)
    time.sleep(0.2)
    m.click(x,y)
    time.sleep(1.5)

    #global sleeptime_count
    #sleeptime_count += 3
    #print sleeptime_count
    # 道士技能
    # if sleeptime_count % 6 == 0:
    #         m.move(400,205)
    #         time.sleep(0.4)
    #         win32api.keybd_event(112 ,0,0,0)     #f1

    # if sleeptime_count % 9 == 0:
    #          win32api.keybd_event(117 ,0,0,0)    #f6


def run():
    no_fond_times = 0
    while True:
        print "[" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "]"
        monsters =  find_monsters()
        l = len(monsters)
        print "monster count:",l
        print monsters
        if l > 0:
            no_fond_times = 0
            target = []
            for monster in monsters:
                if target == []:
                    target = monster
                else:
                    center = [404, 158] #center point
                    ms = math.sqrt(math.pow(center[0] - monster[0], 2) + math.pow(center[1] - monster[1], 2))
                    ts = math.sqrt(math.pow(center[0] - target[0], 2) + math.pow(center[1]- target[1], 2))
                    if ms < ts:
                        target = monster
            last_monster = target
            kill(target)
        else:
            no_fond_times += 1
            if no_fond_times > 5:
                m.click(305, 446, 1)        #random stone
                no_fond_times = 0
            else:
                print "monster no fond, times:",no_fond_times
                direction = [
                    [307, 112],
                    [490, 112],
                    [307, 208],
                    [490, 280],
                ]
                img = ImageGrab.grab((0, 0, 800, 622))
                for p in direction:
                    x = p[0]
                    y = p[1]
                    print x,y
                    temp = 10
                    r = 0
                    g = 0
                    b = 0
                    for j in xrange(0, temp):
                        for i in xrange(0, temp):
                            point = img.getpixel((x + i, y + j))
                            r = r + point[0]
                            g = g + point[1]
                            b = b + point[2]

                    offset = 40
                    if abs(90 - r/(temp * temp)) <= offset and abs(77 - g/(temp * temp)) <= offset and abs(68 - b/(temp * temp)) <= offset:
                        for i in range(10):
                            m.click(x, y, 2)
                            time.sleep(0.5)
                            print "monster repear, move point : ",x,y
                        break

if __name__=="__main__":
    run()
