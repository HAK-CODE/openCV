import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	# convert original frame to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# show video with colors
	cv2.imshow('color', frame)

	# show video with gray
	cv2.imshow('gray', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()