import cv2 as cv
print(cv.__version__)

dispW = 640
dispH = 480

capture = cv.VideoCapture('opencv/InputVideos/meT1.mp4')

outvid = cv.VideoWriter("opencv/OutputVideos/myCam.avi",
                         cv.VideoWriter_fourcc(*"XVID"), 30, (dispW, dispH))

while True:
    isTrue, frame = capture.read()
    frameSize = cv.resize(frame, (dispW, dispH))
    if isTrue:    
        
        cv.imshow('Video', frameSize)
        cv.moveWindow("Video", 0, 0)

        outvid.write(frameSize)

        if cv.waitKey(30) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
outvid.release()
cv.destroyAllWindows()

