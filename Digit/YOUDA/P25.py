import cv2

clicked = False
def onMouse(event , x, y, flags,param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
        

