import cv2 as cv

# # File path to the image
# img_path = "D:/Github/practise-python/ComputerVision/photos/cats/1.jpeg"

# # Load the image
# img = cv.imread(img_path)

# # Display the image
# cv.imshow('Cat', img)
# cv.waitKey(0)

# 0 = webcam, 1 = firstcam, ...

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow("video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
