#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image       # per manipolare immagini
import os                   # per navigare il file system

######----------              M A I N              ----------######

try:
    os.chdir("./screenshots")
except FileNotFoundError:
    os.makedirs("./screenshots/cropped")
    print(
    "Directory create.\n \
    Inserire gli screenshots nella directory apposita e riprovare." )

# rimuovo cornice (e extra spazio) dagli screenshot
for f in os.listdir("./"):
    # f è una stringa contenente il nome del file
    print( "opero su file: ", f)
    if f.endswith(".png"):
        img = Image.open(f)
        print(img.size)
        x1 = 32
        y1 = 35
        x2 = 352
        y2 = 235
        img = img.crop( (x1,y1, x2,y2) )
        print(img.size)
        img.save("./cropped/" + f)

print("gli screenshot senza cornice sono nella directory cropped")
