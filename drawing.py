import cv2 as cv
print(cv.__version__)


capture = cv.VideoCapture('opencv/InputVideos/meT1.mp4')

while True:
    isTrue, frame = capture.read()


    frame = cv.rectangle(frame, (140, 100), (250, 250), (255, 0, 0), 4)
    frame = cv.circle(frame, (320, 240), 25, (0, 0, 255), 4)
    font = cv.FONT_HERSHEY_DUPLEX
    frame = cv.putText(frame, "Hehe", (500, 300), font, 1, (0, 0, 0), 1)
    frame = cv.line(frame, (0, 0), (500, 500), (0, 255, 0), 3)
    frame = cv.arrowedLine(frame, (50, 100), (100, 200), (255, 0, 150), 3)
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(30) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()

