#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import cv2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dist_thresholding(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    matches = bf.knnMatch( des1 , des2 , k = 100)
    newmatches = []
    for item in matches:
        for match in item:
            if match.distance <= threshold_value:
                newmatches.append(match)
    return newmatches

def nn(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    matches = bf.knnMatch( des1 , des2 , k = 1)
    newmatches = []
    for item in matches:
        for match in item:
            if (match.distance <= threshold_value or threshold_value < 0):
                newmatches.append(match)
    return newmatches


def nndr(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    return [0]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
