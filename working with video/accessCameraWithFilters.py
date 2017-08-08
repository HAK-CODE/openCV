import numpy as np 
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
	ret, frame = cap.read()

	out.write(frame)

	# convert original frame to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# show video with colors
	cv2.imshow('color', frame)

	# show video with gray
	cv2.imshow('gray', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
out.release()
cv2.destroyAllWindows()