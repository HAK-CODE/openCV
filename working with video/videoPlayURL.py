import numpy as np 
import cv2

# Provide a url to streaming object
# Connection String --
# rtsp://<USER>:<PASSWORD>@[IP]:[PORT]/cam/realmonitor?channel=[CHANNEL NO.]&subtype=[TYPE NO.]
stream = cv2.VideoCapture('rtsp://admin:123@dmin123@10.16.0.101:554/cam/realmonitor?channel=2&subtype=0')

#if stream is provided 
if stream.isOpened():
	while True:
		ret, frame = stream.read()
		if not ret:
			print('video ended.')
			break
		# Gray scale conversion	
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Show stream on console
		cv2.imshow('frame', gray)

		# Press q to quit
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# Release all resources bounded by system 		
	stream.release()
	cv2.destroyAllWindows()
else:
	print('stream not found.')		