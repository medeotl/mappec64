#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image   # images manipulation
import os               # per navigare il file system
import sys              # per sys.exit("")

def crea_mappa_vuota():
    # calcolo dimensioni opportune
    coordinate_x = set()
    coordinate_y = set()
    for file in os.listdir("./"):
        if file.endswith(".bmp"):
            coordinate_x.add( int( file.split('.')[0] ) )
            coordinate_y.add( int( file.split('.')[1] ) )
    
    min_x = min(coordinate_x)
    max_y = max(coordinate_y)
    base = ( max(coordinate_x) - min_x + 1) * 320
    altezza = ( max_y - min(coordinate_y) + 1) * 200
    mappa = Image.new('P', (base,altezza), 100)
    return mappa, min_x, max_y
        

######----------              M A I N              ----------######

os.chdir("./screenshots")

# rimuovo cornici agli screenshot recenti
for file in os.listdir("./"):
    # file è una stringa contenente il nome del file
    if file.endswith(".bmp"):
        img = Image.open(file)
        print(img.size)
        img = img.crop( (32,35,352,235) )
        print(img.size)
        img.save("./cropped/"+file)
        #~ os.remove(file)

# creo mappa vuota (min_x e max_y servono per conversione coordinate)
os.chdir("./cropped")
mappa, min_x, max_y = crea_mappa_vuota()

# incollo i vari screenshot nella mappa
for file in os.listdir("./"):
    if file.endswith(".bmp"):
        file_x = int( file.split('.')[0] )
        file_y = int( file.split('.')[1] )
        x = (file_x-min_x) * 320 
        y = (max_y-file_y) * 200
        mappa.paste( Image.open(file), (x,y) )

mappa.palette = Image.open(file).palette
#~ mappa.show()
os.chdir("..")
os.chdir("..")
mappa.save("mappa.bmp")


