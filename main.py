import cv2
from simple_facerec import SimpleFacerec as sfr

#camera loading
video_capture = cv2.VideoCapture("")

#Initialize variables
face_locations = []

while True:
	#hold a single frame 
	ret, frame = capture.read()
	
	#rgbtobgr
	rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	
	#finding faces
	face_locations = face_recognition.face_location(rgb)
	
	#result
	for top,right,bottom,left in face_location:
		#frame
		cv2.rectangle = cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
	
	#resultframe
	cv2.imshow('Frame',frame)

	
