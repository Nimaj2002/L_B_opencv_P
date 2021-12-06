# ROI stands for Region of interest

import cv2 as cv
print(cv.__version__)

capture = cv.VideoCapture('opencv/InputVideos/meT1.mp4')

width = capture.get(cv.CAP_PROP_FRAME_WIDTH )
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT )

while True:
    isTrue, frame = capture.read()
    roi = frame[150:350, 250:460].copy() # first y thn x as matrix
    roi_gray = cv.cvtColor(roi, cv.COLOR_BGR2RGB)
    # roi_gray = cv.cvtColor(roi_gray, cv.COLOR_GRAY2BGR)
    frame[150:350, 250:460]=roi_gray
    if isTrue:    
        cv.imshow('Video', frame)
        cv.imshow("Roi", roi)
        cv.imshow("roi_gray", roi_gray)
        cv.moveWindow("Video", 0, 0)
        cv.moveWindow("Roi", int(width)+70, 0)
        
        cv.moveWindow("roi_gray", int(width)+70, 210+50)
        if cv.waitKey(30) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()

