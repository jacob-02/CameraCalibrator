import cv2

cam = cv2.VideoCapture(2)

cv2.namedWindow("test")

img_counter = 0
chessboardSize = (9, 6)
frameSize = (1280, 720)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

while True:
	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow("test", frame)

	if not ret:
		print("failed to grab frame")
		break

	k = cv2.waitKey(1)
	if k % 256 == 27:
		# ESC pressed
		print("Escape hit, closing...")
		break
	elif k % 256 == 32:
		# SPACE pressed
		img_name = "frame_{}.jpg".format(img_counter)
		cv2.imwrite(img_name, frame)
		print("{} written!".format(img_name))
		img_counter += 1

cam.release()
cv2.destroyAllWindows()
