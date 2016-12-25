import cv2
import numpy as np
import sys

class templateMatch:
    def __init__(self, templateUrl, testUrl):
        self.getTemplate(templateUrl)
        self.getMatchingUrl(testUrl)
        self.compare()
        
    def getTemplate(self, templateUrl):
        img_rgb = cv2.imread(templateUrl)
        self.img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        del img_rgb
        cv2.imwrite("input.png", self.img_gray)
        self.img_input = cv2.imread("input.png")
        
    def getMatchingUrl(self, testUrl):
        self.template = cv2.imread(testUrl,0)
        
    def compare(self):
        w, h = self.template.shape[::-1]
        w, h = (w/10), (h/10)
        res = cv2.matchTemplate(self.img_gray,self.template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.85
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(self.img_input, pt, (pt[0] + w, pt[1] + h), (255,255,0), -1)
        lower = np.array([255,255,0])
        upper = np.array([255, 255, 0])
        shapeMask = cv2.inRange(self.img_input, lower, upper)
        _, cnts, _ = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print "Number of matches are %d at confidence score of 85 percent." % len(cnts)
        
if __name__ == "__main__":
    # pass template and test image local URL respectively
    print "Template URL: "
    temp = raw_input()
    print "Test URL: "
    test = raw_input()
    query = templateMatch(temp, test)
    print ""
    print "Press enter key to exit .."
    x = raw_input()
