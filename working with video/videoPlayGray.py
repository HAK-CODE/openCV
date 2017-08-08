import numpy as np 
import cv2

stream = cv2.VideoCapture('files/objects.mp4')

if stream.isOpened():
	while stream.isOpened():
		ret, frame = stream.read()
		if not ret:
			print('video ended.')
			break
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame', gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	stream.release()
	cv2.destroyAllWindows()
else:
	print('stream not found.')		