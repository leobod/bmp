
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
    # data = []
    # for file in f1:
    #     data.append(cv2.imread(file, 0))

    for i in range(0, 111, 1):
        ContourRecognition(f1[i], f2[i])

    print("Hello")


# 处理B类文件夹下的图片
def processB():
    f1 = []
    f2 = []
    for i in range(1, 116, 1):
        f1.append("../../../static/data/B/" + str(i) + ".jpg")
        f2.append("../../../static/data/B2/" + str(i) + ".jpg")

    print(f1)
    print(f2)
    # data = []
    # for file in f1:
    #     data.append(cv2.imread(file, 0))

    for i in range(0, 115, 1):
        ContourRecognition(f1[i], f2[i])

    print("Hello")

processA()
processB()
