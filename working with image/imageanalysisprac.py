import numpy as np 
import cv2

img = cv2.imread('../files/watch.jpg', cv2.IMREAD_COLOR)

print('Pixel values is ', img[55, 55])

img[55, 55] = [0,0,0]

print('Now pixel value is ', img[55, 55])

img[110:150, 100:150] = [255,0,0]

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

