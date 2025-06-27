from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLOv8n model
model = YOLO('yolov8m_best.pt')

# Define path to video file
source = 'col_video.avi'

# Run inference on the source
results = model(source, stream=True, save=True)

# Process results generator
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    

'''from ultralytics import YOLO
import cv2

model = YOLO("yolov8n_best.pt")
cap = cv2.VideoCapture("col_video.mp4")

while cap.isOpened() :
    ret, frame = cap.read()

    if ret :
        results = model(frame)
        cv2.imshow("Results", results[0].plot())

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()'''