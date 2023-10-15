import cv2

VIDEO_PATH = "your_path"

# Open the video file
video_path = VIDEO_PATH
cap = cv2.VideoCapture(video_path)

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame = None

# Read frames until the end of the video
while True:
    ret, frame = cap.read()
    print(f"\n#####\n{ret = }, {frame = } \n####\n")
    if not ret:
        break
    frame2 = frame

# Close the video file
cap.release()

# Check if a frame was read
if frame2 is not None:
    # Save the last frame as image
    cv2.imwrite('last_frame.png', frame2)
    print("Last frame saved as last_frame.png")
else:
    print("Error: Could not read any frames from the video.")
