import cv2
import numpy as np

img_rgb = cv2.imread('sampleTestCase.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imwrite("input.png", img_gray)
img_input = cv2.imread("input.png")

template = cv2.imread('sampleTestCaseTest.jpg',0)
w, h = template.shape[::-1]
w, h = (w/10), (h/10)

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.85
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_input, pt, (pt[0] + w, pt[1] + h), (255,255,0), -1)
    
lower = np.array([255,255,0])
upper = np.array([255, 255, 0])
shapeMask = cv2.inRange(img_input, lower, upper)


_, cnts, _ = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print "I found %d similar shapes" % (len(cnts))


cv2.imshow('Detected',img_input)

cv2.waitKey(0)
cv2.destroyAllWindows()
