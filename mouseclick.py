import cv2 as cv
import numpy as np

def click(event, x, y, flags, params): # function for click events
    global pnt
    global evt
    if event==cv.EVENT_RBUTTONDBLCLK: # Right double click for spoting 
        print("Mouse Event was: ", event)
        print(x, " ", y)
        pnt = (x, y)
        coord.append(pnt)
        print(coord)
        evt = event

    if event==cv.EVENT_LBUTTONDBLCLK: # Left double click for color detection
        print(x, " ", y)
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]
        print(blue, green, red)
        colorString = str(blue) + "," + str(green) + "," + str(red)
        img[:] = [blue, green, red]
        fnt = cv.FONT_HERSHEY_PLAIN
        r = 255-int(red)
        g = 255-int(green)
        b = 255-int(blue)
        tp = (b, g, r)
        cv.putText(img, colorString, (10, 25), fnt, 1, tp, 2)
        cv.imshow("myColor", img)

capture = cv.VideoCapture('opencv/InputVideos/meT1.mp4')
cv.namedWindow("Video")
cv.setMouseCallback("Video", click)

width = capture.get(cv.CAP_PROP_FRAME_WIDTH )
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT )
evt = -1
coord = []
img = np.zeros((240, 240, 3), np.uint8)

while True:
    isTrue, frame = capture.read()

    for pnts in coord:
        cv.circle(frame, pnts, 5, (0, 0 ,255), -1)
        font = cv.FONT_HERSHEY_PLAIN
        myStr = str(pnts)
        cv.putText(frame, myStr, pnts, font, 1.5, (255, 0, 0), 2)

    if isTrue:    
        cv.imshow('Video', frame)
        waitkey = cv.waitKey(30)
        if waitkey & 0xFF==ord('d'): # d for quiting
            break    
        if waitkey == ord("c"): # c for clearing spoted dots
            coord.clear()        
    else:
        break

capture.release()
cv.destroyAllWindows() 