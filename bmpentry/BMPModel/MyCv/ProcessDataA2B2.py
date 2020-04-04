import pandas as pd
import os

from bmpentry.BMPModel.MyCv.WriteDataToCsv import WriteDataToCsv
from bmpentry.BMPModel.MyCv.ColorFilter import RedFilter, GreenFilter

def listfile(dirname="../../../static/data/A2", postfix='.jpg'):
    filelist = []
    files = os.listdir(dirname)
    for item in files:
        if os.path.splitext(item)[1]  == postfix:
                filelist.append(dirname + "/" + item)
        else:
            if os.path.isdir(dirname + item):
                filelist.extend(listfile(dirname + item + '/', postfix))
    return filelist, files

W = WriteDataToCsv(file_path="resultA.csv")
filelist, files = listfile("../../../static/data/A2", postfix=".jpg")

for i in range(0, len(filelist), 1):
    W.appendData("A" + files[i], 160000, RedFilter(filelist[i]), GreenFilter(filelist[i]), "A")

print("hello")

W.write()


W = WriteDataToCsv(file_path="resultB.csv")
filelist, files = listfile("../../../static/data/B2", postfix=".jpg")

for i in range(0, len(filelist), 1):
    W.appendData("B" + files[i], 160000, RedFilter(filelist[i]), GreenFilter(filelist[i]), "B")


print("hello")

W.write()


