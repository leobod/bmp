import cv2
import numpy as np

def RedFilter(file):
    origin = cv2.imread(file, cv2.IMREAD_COLOR)
    dst = cv2.cvtColor(origin, cv2.COLOR_BGR2HSV)
    red_lower_hsv = np.array([0, 43, 46])
    red_upper_hsv = np.array([10, 255, 255])
    mask = cv2.inRange(dst, lowerb=red_lower_hsv, upperb=red_upper_hsv)

    size = 10
    kernel = np.ones((size, size), dtype=np.uint8)
    Dilate = cv2.dilate(mask, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(Dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    redsum = 0
    for cnt in contours:
        unit_area = cv2.contourArea(cnt)
        if unit_area > 1000:
            Border = cv2.drawContours(origin, cnt, -1, (0, 0, 255), 2)
            cv2.imshow("Border", Border)
            redsum += unit_area
    return redsum

def GreenFilter(file):
    origin = cv2.imread(file, cv2.IMREAD_COLOR)
    dst = cv2.cvtColor(origin, cv2.COLOR_BGR2HSV)
    green_lower_hsv = np.array([37, 43, 46])
    green_upper_hsv = np.array([77, 255, 255])
    mask = cv2.inRange(dst, lowerb=green_lower_hsv, upperb=green_upper_hsv)

    size = 10
    kernel = np.ones((size, size), dtype=np.uint8)
    Dilate = cv2.dilate(mask, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(Dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    redsum = 0
    for cnt in contours:
        unit_area = cv2.contourArea(cnt)
        if unit_area > 1000:
            Border = cv2.drawContours(origin, cnt, -1, (0, 0, 255), 2)
            cv2.imshow("Border", Border)
            redsum += unit_area
    return redsum



