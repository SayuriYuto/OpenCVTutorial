import cv2 as cv
#RESIZING AND RE SCALING
img = cv.imread('Resources/Photos/cat_large.jpg') #read image into an image matrix

def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

def changeRes(width,height):
    #only for live feed from webcam
    capture_webcam.set(3,width)
    capture_webcam.set(4,height)

# img_resized = rescaleFrame(img,0.5)
# cv.imshow('catlarge',img)
# cv.imshow('catlarge_resized',img_resized)
# cv.waitKey(0)

# capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# while True:
#     isTrue,frame = capture.read()
#     cv.imshow('dog',frame)
#     cv.imshow('dog resized',rescaleFrame(frame))
#     if cv.waitKey(24)& 0xFF == ord('d'):
#         break
# capture.release() 

capture_webcam = cv.VideoCapture(0)
while True:
    isTrue,frame = capture_webcam.read()
    cv.imshow('webcam',frame)
    cv.imshow('webcam resized',rescaleFrame(frame))
    cv.imshow('changed resolution',changeRes(100,100))
    if cv.waitKey(24)& 0xFF == ord('d'):
        break
capture_webcam.release() 

cv.destroyAllWindows()