import cv2

videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # CAP DOWN to hide the warning

ret, frame = videoCaptureObject.read()
cv2.imwrite("picture.jpg", frame)

videoCaptureObject.release()
cv2.destroyAllWindows()
