#!/usr/bin/python3

from Compos import BETTER, COMPOS_LIST
from ChampionList import CHAMPION_LIST
import sys
import cv2
import numpy as np
import os.path
from os import path
import pyautogui
import keyboard
from matplotlib import pyplot as plt
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller

def getChampionCoords(champion):
    img_rgb = cv2.imread('tft.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('champions/%s.png' % champion,0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    res = []
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.imwrite('res.png',img_rgb)
        res.append(pt)
    return res

def printComps():
    for comp in COMPOS_LIST:
        print (comp.name+":")
        for ch in comp.champs:
            print (ch.name)
        print ("\n")

def click(x,y):
    mouse = MouseController()
    mouse.position = (x, y)
    mouse.press(Button.left)
    pyautogui.sleep(0.1)
    mouse.release(Button.left)

def main(args):
    while True:
        if keyboard.is_pressed("q"):
            break
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r"tft.png")
        for champ in BETTER.champs:
            if path.exists('champions/%s.png' % champ.name):
                coor = getChampionCoords(champ.name)
                for co in coor:
                    click(co[0], co[1])
                    print (champ.name, sorted(coor, key=lambda champion: champion[0]))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)