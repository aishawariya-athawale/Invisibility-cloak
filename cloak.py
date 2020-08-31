import cv2
import numpy as np

cap = cv2.VideoCapture(0) # Capture from the integrated webcam
background = cv2.imread('Background.jpg')

while True:
    ret, frame = cap.read()

    if ret:
        color_to_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converting frame from RGB to HSV
        
        # Creating mask to detect blue color
        lower_blue = np.array([75,80,10])
        upper_blue = np.array([120,255,255])

        mask_blue = cv2.inRange(color_to_hsv,lower_blue,upper_blue)

        # Clean out the cloak's edges
        mask_blue = cv2.morphologyEx(mask_blue,cv2.MORPH_OPEN, np.ones((7,7),np.uint8)) #Applying OPENING using the OPEN function
        # mask_blue = cv2.morphologyEx(mask_blue,cv2.MORPH_DILATE, np.ones((7,7),np.uint8)) # Applying OPENING using Dilation & Erosion 
        # mask_blue = cv2.morphologyEx(mask_blue,cv2.MORPH_ERODE, np.ones((7,7),np.uint8))
        
        # Displaying the background
        background_mask = cv2.bitwise_and(background, background, mask = mask_blue)
        
        # Hiding the blue part      
        mask_not = cv2.bitwise_not(mask_blue)
        
        # Removing blue color from the frame
        things_behind_mask = cv2.bitwise_and(frame, frame, mask=mask_not)
        
        # Displaying the background of the frame (cloak is ready)
        cv2.imshow("cloak", background_mask+things_behind_mask)
        
        if cv2.waitKey(2) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
