import numpy 
import cv2

#get stream from system camera
stream = cv2.VideoCapture(0)

while(True):
	ret, frame = stream.read()				#read stream from camera
	cv2.imshow('frame', frame)				#render stream on console
	if cv2.waitKey(1) & 0xFF == ord('q'):	#user input to quit
		break

stream.release()
cv2.destroyAllWindows()