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

W = WriteDataToCsv(file_path="second_csv/resultAA.csv")
filelist, files = listfile("../../../static/data/AAAA2/AA", postfix=".jpg")
for i in range(0, len(filelist), 1):
    W.appendData("AA" + files[i], 160000, RedFilter(filelist[i]), GreenFilter(filelist[i]), "AA")
print("hello")
W.write()


W = WriteDataToCsv(file_path="second_csv/resultAB.csv")
filelist, files = listfile("../../../static/data/AAAA2/AB", postfix=".jpg")
for i in range(0, len(filelist), 1):
    W.appendData("AB" + files[i], 160000, RedFilter(filelist[i]), GreenFilter(filelist[i]), "AB")
print("hello")
W.write()


W = WriteDataToCsv(file_path="second_csv/resultBA.csv")
filelist, files = listfile("../../../static/data/AAAA2/BA", postfix=".jpg")
for i in range(0, len(filelist), 1):
    W.appendData("BA" + files[i], 160000, RedFilter(filelist[i]), GreenFilter(filelist[i]), "BA")
print("hello")
W.write()


W = WriteDataToCsv(file_path="second_csv/resultBB.csv")
filelist, files = listfile("../../../static/data/AAAA2/BB", postfix=".jpg")
for i in range(0, len(filelist), 1):
    W.appendData("BB" + files[i], 160000, RedFilter(filelist[i]), GreenFilter(filelist[i]), "BB")
print("hello")
W.write()


