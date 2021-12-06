import cv2 as cv
print(cv.__version__)

def nothing(x):
    pass
capture = cv.VideoCapture('opencv/InputVideos/meT1.mp4')

width = capture.get(cv.CAP_PROP_FRAME_WIDTH )
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT )

cv.namedWindow("Video")
cv.createTrackbar("xVal", "Video", 0, int(width), nothing)

while True:
    isTrue, frame = capture.read()
     
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(30) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()