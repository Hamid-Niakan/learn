import os
import sys
import re
import time


inputs = sys.argv
src = inputs[1]
dist = inputs[2]
if not (os.path.isdir(dist)):
    os.mkdir(dist)

docs = os.walk(src)


def makeDist(fileType, year, fileName):
    fileAddr = os.path.join(dist, year)
    if not (os.path.isdir(fileAddr)):
        os.mkdir(fileAddr)
    fileAddr = os.path.join(dist, year, fileType)
    if not (os.path.isdir(fileAddr)):
        os.mkdir(fileAddr)
    fileAddr = os.path.join(dist, year, fileType, fileName)
    return fileAddr


for root, dirs, files in docs:
    for fileName in files:
        fileType = ""
        if bool(re.match(".+\.(jpg|jpeg|png)$", fileName.lower())):
            fileType = "photos"
        elif bool(re.match(".+\.(mp4|avi|3gp|mpeg|mkv|wmv|mov)$", fileName.lower())):
            fileType = "videos"
        else:
            continue
        fileAddr = os.path.join(root, fileName)
        year = time.ctime(os.path.getmtime(fileAddr)).split()[-1]
        with open(fileAddr, 'rb') as src:
            data = src.read()
            with open(makeDist(fileType, year, fileName), 'wb') as dst:
                dst.write(data)
