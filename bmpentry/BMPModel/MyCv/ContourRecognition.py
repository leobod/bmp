import cv2
import numpy as np
import matplotlib.pyplot as plt

# 寻找细胞的中心，与半径
def findCenter(src, cnt):
    raw_dist = np.empty(src.shape, dtype=np.float)
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            raw_dist[i,j] = cv2.pointPolygonTest(cnt, (j,i), True)

    minVal, maxVal, _, maxDistPt = cv2.minMaxLoc(raw_dist[:, :, 2])
    minVal = abs(minVal)
    maxVal = abs(maxVal)

    return maxVal, maxDistPt

def ContourRecognition(file, file2=None):
    Origin = cv2.imread(file, cv2.IMREAD_ANYCOLOR)
    Origin = cv2.cvtColor(Origin, cv2.COLOR_BGR2HSV)
    V = Origin[:, :, 2]
    zeros = np.zeros(Origin.shape[:2], dtype="uint8")
    Origin = cv2.merge([zeros, zeros, V])
    Origin = cv2.cvtColor(Origin, cv2.COLOR_HSV2BGR)
    Origin = cv2.cvtColor(Origin, cv2.COLOR_BGR2GRAY)
    Gaussian = cv2.GaussianBlur(Origin, (5, 5), 0)

    ret, th = cv2.threshold(Gaussian, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    size = 35
    kernel = np.ones((size, size), dtype=np.uint8)
    Dilate = cv2.dilate(th, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(Dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img2 = cv2.imread(file, cv2.IMREAD_ANYCOLOR)
    Border = cv2.drawContours(img2, contours, -1, (0, 0, 255), 2)

    for cnt in contours:
        unit_area = cv2.contourArea(cnt)
        if unit_area >= 30000:
            radius, center = findCenter(Border, cnt)
            radius = int(radius)
            w, h, c = Border.shape
            blank = np.zeros((w, h, c), np.uint8)
            blank.fill(255)
            blank = cv2.circle(blank, center, radius, [0, 0, 0], -1)

            Border = cv2.circle(img2, center, int(radius), (0, 255, 0), 2)
            img3 = cv2.imread(file, cv2.IMREAD_ANYCOLOR)
            Result = cv2.add(img3, blank)
            Result = Result[center[1]-radius:center[1]+radius, center[0]-radius:center[0]+radius,:]
            Result = cv2.resize(Result, (400, 400), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(file2, Result)
            print(1)
            return Result
    return None

a01 = ContourRecognition("./111.jpg", "./111_2.jpg")


print("hello")

cv2.waitKey(0)

