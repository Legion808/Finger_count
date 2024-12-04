import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to detect fire in a frame
def detect_fire(frame):
    # Convert the frame to HSV (Hue, Saturation, Value) color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for detecting fire color in HSV
    lower_bound = np.array([18, 50, 50], dtype="uint8")
    upper_bound = np.array([35, 255, 255], dtype="uint8")

    # Create a mask with the specified fire color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Perform bitwise AND to isolate the fire color in the frame
    fire_detected = cv2.bitwise_and(frame, frame, mask=mask)

    return fire_detected, mask

# Function to show frames using matplotlib
def show_frame_matplotlib(frame, title="Frame"):
    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# Open video capture from webcam
cap = cv2.VideoCapture(0)  # Use '0' for webcam, or provide path for video file

if not cap.isOpened():
    print("Error: Could not open video stream.")
else:
    print("Video stream opened successfully!")

# Process video frames in a loop
while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    if not ret:
        print("Failed to capture frame.")
        break  # Exit the loop if frame capture fails

    # Detect fire in the current frame
    fire_detected, fire_mask = detect_fire(frame)

    # Show the original frame and fire detection
    show_frame_matplotlib(frame, "Original Video")
    show_frame_matplotlib(fire_detected, "Fire Detected")

    # Check if the user wants to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
