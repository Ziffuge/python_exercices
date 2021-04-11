
import os
import shutil

source = "boule de feu.jpg"
target = "images/boule de feu.jpg"

shutil.copy(source, target)
os.remove(source)