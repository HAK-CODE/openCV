import numpy as np 
import cv2

img = cv2.imread('../files/watch.jpg', cv2.IMREAD_COLOR)

# DRAWING A LINE
# cv2.line(image reference, where to start (x,y), where to end (x,y), color of line (B, G, R), width of line (x))
cv2.line(img, (0, 0), (150, 150), (0, 255, 0), 15)

# DRAWING A RECTANGLE
# cv2.ractangle(img, whare to start (x,y), where to end (x,y), (B, G, R), width (x))
cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 20)

# DRAWING A CIRCLE
# cv2.circle(image refrence, where is centre of circle (x,y), where is radius of circle (x), (B, G, R), -1 (to fill in with color))
cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

# DRAW A POLYGON
pts = np.array([[10,5], [20, 30], [70, 20], [50, 10]], np.int32)
# cv2.polylines(image reference, points array, bool for joining points or not, (B, G, R), line width)
cv2.polylines(img, [pts], True, (255, 0, 0), 3)

# FONT
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Pro!', (0, 130), font, 1, (200, 255, 200), 2, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
