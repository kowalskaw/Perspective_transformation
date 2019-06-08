import cv2
import numpy as np
from matplotlib import pyplot as plt

l: list = []
img = None
img_cp = None


def draw_circle(event, x, y, flags, param):
    global l
    global img
    global img_cp
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_cp, (x, y), 5, (255, 0, 0), -1)
        l.append([x, y])
        cv2.imshow('image', img_cp)

    if len(l) == 4:
        print(l)

        pts1 = np.float32(l)
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(img, M, (300, 300))

        cv2.imshow('Original image', img_cp)
        cv2.imshow('Final', dst)
        img_cp = img.copy()
        l.clear()


def road_straight():
    global img
    global img_cp
    img = cv2.imread('road.jpg')
    img = cv2.resize(img, dsize=(1000, 1000))
    img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75, interpolation=cv2.INTER_NEAREST)
    img_cp = img.copy()
    cv2.namedWindow('image')
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', draw_circle)

    cv2.waitKey()
    cv2.destroyAllWindows()
    return


road_straight()
