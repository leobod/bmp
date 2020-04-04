import cv2
import numpy as np

def createHist(img):
    h, w, c = img.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = img[row, col, 0]
            g = img[row, col, 1]
            r = img[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist

def HistCompare(img1, img2):
    hist1 = createHist(img1)
    hist2 = createHist(img2)
    match1 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
    match2 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    match3 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
    print("巴氏: %s  相关性: %s   卡方: %s" %(match1, match2, match3))
    return match1, match2, match3

a1 = cv2.imread("./01.jpg", cv2.IMREAD_ANYCOLOR)
a2 = cv2.imread("./02.jpg", cv2.IMREAD_ANYCOLOR)
a3 = cv2.imread("./03.jpg", cv2.IMREAD_ANYCOLOR)
a4 = cv2.imread("./04.jpg", cv2.IMREAD_ANYCOLOR)
a5 = cv2.imread("./05.jpg", cv2.IMREAD_ANYCOLOR)
a6 = cv2.imread("./test.png", cv2.IMREAD_ANYCOLOR)



HistCompare(a1, a6)
HistCompare(a1, a2)
HistCompare(a1, a3)
HistCompare(a1, a4)
HistCompare(a1, a5)
