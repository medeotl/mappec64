#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image       # per manipolare immagini
import os                   # per navigare il file system

def crea_mappa_vuota():
    # calcolo dimensioni opportune
    coordinate_x = set()
    coordinate_y = set()
    for f in os.listdir("./"):
        if f.endswith(".bmp"):
            coordinate_x.add( int( f.split('.')[0] ) )
            coordinate_y.add( int( f.split('.')[1] ) )

    min_x = min(coordinate_x)
    max_y = max(coordinate_y)
    base = ( max(coordinate_x) - min_x + 1) * (x2-x1)
    altezza = ( max_y - min(coordinate_y) + 1) * (y2-y1)
    mappa = Image.new('P', (base,altezza), 100)
    return mappa, min_x, max_y


######----------              M A I N              ----------######

try:
    os.chdir("./screenshots")
except FileNotFoundError:
    os.makedirs("./screenshots/cropped")
    print(
    "Directory create.\n \
    Inserire gli screenshots nella directory apposita e riprovare." )

# rimuovo cornici (e extra spazio) dagli screenshot
for f in os.listdir("./"):
    # file è una stringa contenente il nome del file
    if f.endswith(".bmp"):
        img = Image.open(f)
        print(img.size)
        x1 = 32
        y1 = 35
        x2 = 352
        y2 = 211
        img = img.crop( (x1,y1, x2,y2) )
        print(img.size)
        img.save("./cropped/"+f)

# creo mappa vuota (min_x e max_y servono per conversione coordinate)
os.chdir("./cropped")
mappa, min_x, max_y = crea_mappa_vuota()

# incollo i vari screenshot nella mappa
for f in os.listdir("./"):
    if f.endswith(".bmp"):
        file_x = int( f.split('.')[0] )
        file_y = int( f.split('.')[1] )
        x = (file_x-min_x) * (x2-x1)
        y = (max_y-file_y) * (y2-y1)
        mappa.paste( Image.open(f), (x,y) )
        os.remove(f)



mappa.palette = Image.open(f).palette

# rimuovo gli screenshoot in cropped


os.chdir("..")
os.chdir("..")
mappa.save("mappa.bmp")

#TODO
