#coding=utf-8
import os
from PIL import Image
from PIL import ImageGrab
from pymouse import PyMouse
import time
import random
import win32api
import win32con

m = PyMouse()
sleeptime_count = 0


def find_monsters():
    img = ImageGrab.grab((0, 0, 800, 622))
    size = img.size
    
    points = []
    monsters = []
    for j in range(size[1]):
        if j >= 380:
            break
        for i in range(size[0]):
            if i >= 710 and j >= 340:
                break
            point = img.getpixel((i,j))
            offset = 70
            if points == []:
                if abs(0 - point[0]) <= offset and abs(0 - point[1]) <= offset and abs(0 - point[2]) <= offset:
                    points.append([i,j])
            else:
                offset2 = 50
                if abs(255 - point[0]) <= offset2 and abs(0 - point[1]) <= offset2 and abs(0 - point[2]) <= offset2:
                    if  j == points[-1][1] and i - points[-1][0] == 1:
                        points.append([i,j])
                else:
                    points = []
            
            if len(points) > 3:
                print "monster:",points
                monsters.append(points[0])
                points = []

    return monsters


def kill(p):
    x = p[0] + 16
    y = p[1] + 59
    m.click(x,y)
    time.sleep(2)
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
    last_monster = []
    no_fond_times = 0
    repeat_count = 0

    while True:
        print "[" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "]"
        monsters =  find_monsters()
        
        if len(monsters) > 0:      
            no_fond_times = 0
            target = []
            i = 0
            l = len(monsters)
            
            for monster in monsters:
                    if abs(338 - monster[0]) < 5 and monster[1] >= 125 - 5 and monster[1] <= 189 + 5:
                        target = monster
                        break
                    if abs(434 - monster[0]) < 5 and monster[1] >= 125 - 5 and monster[1] <= 189 + 5:
                        target = monster
                        break
                    if abs(386 - monster[0]) < 5 and monster[1] >= 125 - 5 and monster[1] <= 189 + 5:
                        target = monster
                        break
                    i += 1
            
            if target == []:
                i = l / 2
                if i > 2:
                    i -= 1
                target = monsters[i]

            if target == last_monster:
                repeat_count += 1
                print "monster repear times : ",repeat_count
            else:
                repeat_count =  0

            if repeat_count > 2:
                x = random.randint(700, 800)
                y = random.randint(50, 370)

                m.click(x, y, 2)
                print "monster repear, move point : ",x,y

                
                i = random.randint(0, l - 1)
                target = monsters[i]
                
            if repeat_count > 5:
                m.click(305, 446, 1)        #random stone
                continue
                            
            print "monster count:",l,", current monster index:",i

            last_monster = target    
            kill(target)
            
            monsters = find_monsters()
            for monster in monsters:
                if target == monster:    # target is exist
                    kill(target)
                    break
        else:
            no_fond_times += 1
            print "monster no fond, times:",no_fond_times
        if no_fond_times > 3:
            x = random.randint(700, 800)
            y = random.randint(50, 370)
            m.click(x, y, 2)
            print "onster no fond, move point : ",x,y
            time.sleep(1.5)
        if no_fond_times > 15:
            m.click(305, 446, 1)        #random stone
            no_fond_times = 0


if __name__=="__main__":
    run()
