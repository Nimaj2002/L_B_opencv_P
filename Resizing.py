import cv2 as cv
print(cv.__version__)


capture = cv.VideoCapture('opencv/meT1.mp4')

while True:
    isTrue, frame = capture.read()
    frameSmall = cv.resize(frame, (320, 240))
    if isTrue:    
        cv.imshow('Video', frameSmall)
        cv.moveWindow("Video", 0, 0)

        if cv.waitKey(30) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
