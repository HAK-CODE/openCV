import numpy as np 
import cv2

stream = cv2.VideoCapture(0)

if stream.isOpened():
	while(True):
		ret, frame = stream.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	#changing frame to gray
		cv2.imshow('frame', gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
else:
	print('stream not found.')
stream.release()
cv2.destroyAllWindows()
