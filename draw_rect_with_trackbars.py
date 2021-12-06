import cv2 as cv
print(cv.__version__)

def nothing(x):
    pass

capture = cv.VideoCapture('opencv/InputVideos/meT1.mp4')
cv.namedWindow("Video")

width = capture.get(cv.CAP_PROP_FRAME_WIDTH )
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT )

cv.createTrackbar("width", "Video", 100, 500, nothing)
cv.createTrackbar("height", "Video", 100, 500, nothing)
cv.createTrackbar("xval", "Video", 100, int(width), nothing)
cv.createTrackbar("yval", "Video", 100, int(height), nothing)


while True:
    isTrue, frame = capture.read()

    xval = cv.getTrackbarPos("xval", "Video")
    yval = cv.getTrackbarPos("yval", "Video")
    width = cv.getTrackbarPos("width", "Video")
    height = cv.getTrackbarPos("height", "Video")
    
    cv.rectangle(frame, (xval, yval), (xval+width, yval+height), (0, 255, 0), 3)

    if isTrue:    
        
        cv.imshow('Video', frame)
        cv.moveWindow("Video", 0, 0)
        if cv.waitKey(30) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()

