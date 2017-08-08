import numpy as np 
import cv2

#set path or put filename to play
stream = cv2.VideoCapture('files/objects.mp4')

if stream.isOpened():
	while(stream.isOpened()):
		ret, frame = stream.read()
		if not ret:
			print('video ended.')
			break
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	stream.release()
	cv2.destroyAllWindows()		
else:
	print('stream not found.')
