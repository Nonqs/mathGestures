import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the frame
cap.set(4, 720)  # Set the height of the frame

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHandInfo(img):
    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
       
        hand = hands[0]  
        lmList = hand["lmList"]  # List of 21 landmarks for the first hand

        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    else:
        return None
    
def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, current_pos, prev_pos, (255, 0, 255), 10)
        
    return current_pos


prev_pos = None   
canvas = None
image_combined = None

# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    if canvas is None:
        canvas = np.zeros_like(img)
    
    
    info = getHandInfo(img)
    if info:
        fingers, lmList = info
        print(fingers)
        prev_pos = draw(info, prev_pos, canvas)
        
    image_combined = cv2.addWeighted(img, 0.7, canvas, 0.5, 0)

    # Display the image in a window
    cv2.imshow("Image", img)
    cv2.imshow("Canvas", canvas)
    cv2.imshow("Combined", image_combined)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)
