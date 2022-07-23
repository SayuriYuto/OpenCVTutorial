import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg') #read image
cv.imshow('Cat',img) #display image in a window titled "Cat" with image
cv.waitKey(0) #keep window open till a keypress