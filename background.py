import cv2

cap = cv2.VideoCapture(0) # For the integrated webcam

while True:
    ret, img = cap.read()

    if ret:
        cv2.imshow("Background", img)

        if cv2.waitKey(2) == ord('q'):
             cv2.imwrite("Background.jpg", img)
             break
cap.release()
cv2.destroyAllWindows()