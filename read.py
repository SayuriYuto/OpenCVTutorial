from string import hexdigits
from turtle import width
from xml.dom.minidom import DOMImplementation
import cv2 as cv

#READING IMAGES
'''
img = cv.imread('Resources/Photos/cat.jpg') #read image into an image matrix
# print(img)
cv.imshow('Cat',img) #display image in a window titled "Cat" with image
cv.waitKey(0) #keep window open till a keypress
'''

#READING VIDEOS
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
#VideoCapture(0.) = webcam

while True:
    isTrue,frame = capture.read() #grab video frame by frame
    cv.imshow('Video',frame) #display each frame
    if cv.waitKey(24) & 0xFF == ord('d'): #if letter d is pressed break out of the loop, ord() returns the ascii value of char
        break

capture.release()
cv.destroyAllWindows()