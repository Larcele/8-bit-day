#!/usr/bin/env python

import datetime
import os
import shutil
import time

#set the PATH to where all your BitDay images are
PATH = 				"/home/larcele/PycharmProjects/bgChanger/"

#the currently set wallpaper
CURRENT = 			"current.png"

Early_Morning = 	'01-Early-Morning.png'
Mid_Morning = 		'02-Mid-Morning.png'
Late_Morning = 		'03-Late-Morning.png'
Early_Afternoon = 	'04-Early-Afternoon.png'
Mid_Afternoon = 	'05-Mid-Afternoon.png'
Late_Afternoon = 	'06-Late-Afternoon.png'
Early_Evening = 	'07-Early-Evening.png'
Mid_Evening = 		'08-Mid-Evening.png'
Late_Evening = 		'09-Late-Evening.png'
Early_Night = 		'10-Early-Night.png'
Mid_Night = 		'11-Mid-Night.png'
Late_Night = 		'12-Late-Night.png'

time = datetime.datetime.now().hour

# Gets out the new wallpaper based on the current hour of the day

if 3 <= time <= 4:
    shutil.copy(PATH + Early_Morning, PATH + CURRENT)

elif 5 <= time <= 6:
    shutil.copy(PATH + Mid_Morning, PATH + CURRENT)

elif 7 <= time <= 8:
    shutil.copy(PATH + Late_Morning, PATH + CURRENT)

elif 9 <= time <= 10:
    shutil.copy(PATH + Early_Afternoon, PATH + CURRENT)

elif 11 <= time <= 12:
    shutil.copy(PATH + Mid_Afternoon, PATH + CURRENT)

elif 13 <= time <= 14:
    shutil.copy(PATH + Late_Afternoon, PATH + CURRENT)

elif 15 <= time <= 17:
    shutil.copy(PATH + Early_Evening, PATH + CURRENT)

elif 18 <= time <= 19:
    shutil.copy(PATH + Mid_Evening, PATH + CURRENT)

elif 20 <= time <= 21:
    shutil.copy(PATH + Late_Evening, PATH + CURRENT)

elif 22 <= time <= 23:
    shutil.copy(PATH + Early_Night, PATH + CURRENT)

elif 0 <= time <= 1:
	shutil.copy(PATH + Mid_Night, PATH + CURRENT)

elif  2 <= time <= 3:
    shutil.copy(PATH + Late_Night, PATH + CURRENT)

# Set the background image
os.system("gsettings set org.cinnamon.desktop.background picture-uri \"file:///" + PATH + CURRENT + "\"")
print("OK")
