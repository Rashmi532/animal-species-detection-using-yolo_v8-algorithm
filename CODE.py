from ultralytics import YOLO
import cv2
from beeply.notes import *
import smtplib

# Load the custom YOLOv8 model
model_path = "./best.pt"  # Replace with the path to your trained YOLOv8 model
model = YOLO(model_path)

def mail_send(msg):
    usermail = 'jebishaj03@gmail.com'
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('nayanaramanth2003@gmail.com','niac lmkx evas bybq')
    s.sendmail('jebishaj03@gmail.com', usermail,msg)
    s.quit()
    print('Mail send')

# Initialize video capture (camera or video file)
#cap = cv2.VideoCapture(0)# Replace 0 with "path_to_video.mp4" for a video file
cap = cv2.VideoCapture('./clg.mp4')
# Check if video capture is successful

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

#img=cv2.imread('./1.jpg')
cls=10
while True:
    # Read a frame from the video
    
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    #frame =img

    # Run the YOLOv8 model on the frame
    results = model(frame)
    
    # Loop through detections and draw bounding boxes
    for r in results:
        for box in r.boxes:
            # Extract box coordinates, confidence, and class
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            conf = box.conf[0]  # Confidence score
            cls = int(box.cls[0])  # Class ID
            label = model.names[cls]  # Class name
            
            if label == 'ELEPHANT':
                label=''
                conf=''
            else:

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Add label and confidence
                text = f"{label} {conf:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                
    # Display the frame with detections
    cv2.imshow("YOLOv8 Object Detection", frame)
    try:
        if cls==10 or cls == 2:
            pass
        else:
            
            a=beeps(1154)
            a.hear('A_')
            #a.hear('A_',5000)
            print('Done')
            cls=10
            mail_send(text)
    except:
        pass

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

#cd C:\Users\nayan\Desktop\animal_using yolov8
#python test.py
