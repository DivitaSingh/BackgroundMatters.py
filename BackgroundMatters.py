import cv2
import numpy as np

#to start the video capture
cap = cv2.VideoCapture(0)

#to read the image
#imread(): This function is used to read images and takes the following 2 arguments:
image = cv2.imread('bangkok.jpg')

while True:
        ret, frame = cap.read()

        frame = cv2.resize(frame, (640, 480))
        image = cv2.resize(image, (640, 480))

        u_black = np.array([104,153,70])
        l_black = np.array([30,30,0])

        mask = cv2.inRange(frame, u_black, l_black)
        res = cv2.bitwise_and(frame, frame, mask = mask)

        f = frame - res
        f = np.where( f == 0, image, f)

#to show the image
#imshow(): This function is used to display images and takes the following two arguments:
        real_vid = cv2.imshow('frame',frame)
        masked_vid = cv2.imshow('f',f)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()

