import cv2 as cv
print(cv.__version__)


capture = cv.VideoCapture('opencv/meT1.mp4')

while True:
    isTrue, frame = capture.read()
     
    if isTrue:    
        cv.imshow('Video', frame)
        cv.moveWindow("Video", 0, 0)
 
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("Gray", gray)
        cv.moveWindow("Gray", 705, 0)


        rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        cv.imshow("RGB", rgb)
        cv.moveWindow("RGB", 0, 530)

        if cv.waitKey(30) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()