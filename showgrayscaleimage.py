import cv2
import numpy as np 

# cv2.IMREAD_GRAYSCALE for setting alpha to 0
img = cv2.imread('files/watch.jpg', cv2.IMREAD_GRAYSCALE)

# we can also use 0 as second parameter for grayscale image
#img = cv2.imread('files/watch.jpg', 0)

# first param is used for setting the title of image show
cv2.imshow('image', img)

# wait for any key to press
cv2.waitKey(0)

cv2.destroyAllWindows()