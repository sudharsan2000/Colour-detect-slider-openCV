import cv2
import numpy as np


def nothing(x):
    pass


camera = cv2.VideoCapture(0)

hue = 'Hue'
sat = 'Saturation'
value = 'Value'
wnd = 'Colorbars'
cv2.namedWindow(wnd, flags=cv2.WINDOW_AUTOSIZE)
# Begin Creating trackbars for each
cv2.createTrackbar(hue, wnd, 0, 255, nothing)

cv2.createTrackbar(sat, wnd, 0, 255, nothing)

cv2.createTrackbar(value, wnd, 0, 255, nothing)
while(1):
    _, frame = camera.read()
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    cv2.imshow('Frame', frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos(hue, wnd)
    s = cv2.getTrackbarPos(sat, wnd)
    v = cv2.getTrackbarPos(value, wnd)

    lower_range = np.array([h-25, s-25, v-25])
    upper_range = np.array([h+25, s+25, v+25])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    original_color = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('masked', original_color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(' H:' ,h ,' S: ' ,s ,' V: ', v)
        break
camera.release()
cv2.destroyAllWindows()
