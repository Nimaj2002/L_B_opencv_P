import cv2 as cv
print(cv.__version__)

capture = cv.VideoCapture('opencv/InputVideos/meT1.mp4')

width = capture.get(cv.CAP_PROP_FRAME_WIDTH )
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT )
# print(width, height)
start_po = (int(width//2), int(height//2))
x_movement = +5
y_movement = +5

while True:
    end_po = (start_po[0]+100, start_po[1]+50)
    isTrue, frame = capture.read()
    frame = cv.rectangle(frame, start_po, end_po, (0, 0 ,255), -1)    
    cv.imshow('Video', frame)
        
    if start_po[1] >= height-50 or start_po[1] <= 0:
        y_movement = -y_movement

    if start_po[0] > width-100 or start_po[0] < 0:
        x_movement = -x_movement

    start_po = (start_po[0]+x_movement, start_po[1]+y_movement)

    if cv.waitKey(30) & 0xFF==ord('d'):
        break            

capture.release()
cv.destroyAllWindows()