
import cv2

from bmpentry.BMPModel.MyCv.ContourRecognition import ContourRecognition

#  读取A类文件夹下的图片
def processA():
    f1 = []
    f2 = []
    for i in range(1, 112, 1):
        f1.append("../../../static/data/A/" + str(i) + ".jpg")
        f2.append("../../../static/data/A2/" + str(i) + ".jpg")
    print(f1)
    print(f2)
    for i in range(0, 111, 1):
        ContourRecognition(f1[i], f2[i])

    print("Hello")

#  读取B类文件夹下的图片
def processB():
    f1 = []
    f2 = []
    for i in range(1, 116, 1):
        f1.append("../../../static/data/B/" + str(i) + ".jpg")
        f2.append("../../../static/data/B2/" + str(i) + ".jpg")
    print(f1)
    print(f2)
    for i in range(0, 115, 1):
        ContourRecognition(f1[i], f2[i])
    print("Hello")

#  读取AA类文件夹下的图片
def processAA():
    f1 = []
    f2 = []
    for i in range(1, 33, 1):
        f1.append("../../../static/data/AAAA/AA/" + str(i) + ".jpg")
        f2.append("../../../static/data/AAAA2/AA/" + str(i) + ".jpg")
    print(f1)
    print(f2)
    for i in range(0, 32, 1):
        ContourRecognition(f1[i], f2[i])

    print("Hello")


# 处理AB类文件夹下的图片
def processAB():
    f1 = []
    f2 = []
    for i in range(1, 14, 1):
        f1.append("../../../static/data/AAAA/AB/" + str(i) + ".jpg")
        f2.append("../../../static/data/AAAA2/AB/" + str(i) + ".jpg")
    print(f1)
    print(f2)
    for i in range(0, 13, 1):
        ContourRecognition(f1[i], f2[i])
    print("Hello")

# 处理BA类文件夹下的图片
def processBA():
    f1 = []
    f2 = []
    for i in range(1, 44, 1):
        f1.append("../../../static/data/AAAA/BA/" + str(i) + ".jpg")
        f2.append("../../../static/data/AAAA2/BA/" + str(i) + ".jpg")
    print(f1)
    print(f2)
    for i in range(0, 43, 1):
        ContourRecognition(f1[i], f2[i])

    print("Hello")


# 处理BA类文件夹下的图片
def processBB():
    f1 = []
    f2 = []
    for i in range(1, 115, 1):
        f1.append("../../../static/data/AAAA/BB/" + str(i) + ".jpg")
        f2.append("../../../static/data/AAAA2/BB/" + str(i) + ".jpg")
    print(f1)
    print(f2)
    for i in range(0, 114, 1):
        ContourRecognition(f1[i], f2[i])

    print("Hello")


# processAA()
# processAB()
# processBA()
processBB()
