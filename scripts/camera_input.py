import cv2
import numpy as np

IP_ADDRESS = "10.202.2.127:8080"
url = "http://"+IP_ADDRESS+"/video"

cam = cv2.VideoCapture(url)

while(True):
    camera, frame = cam.read()
    if frame is not None:
        cv2.imshow(IP_ADDRESS, frame)

    q = cv2.waitKey(1)
    if q==ord("q"):
        break

cv2.destroyAllWindows()