import cv2
import torch

try:
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)
except Exception as e:
    if "PosixPath" in str(e):
        model = torch.load('best.pt', map_location=torch.device('cpu'))
        model = model['model']  
    else:
        raise e  


cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    detections = results.pandas().xyxy[0]

    threat_detected = False
    for i in range(len(detections)):
        label = detections.iloc[i]['name']
        if label in ['Guns', 'Rifle', 'Knife']:  
            threat_detected = True
            break

    if threat_detected:
        cv2.putText(frame, "Threat", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # Red text
    else:
        cv2.putText(frame, "No Threat", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Green text

    for i in range(len(detections)):
        xmin = int(detections.iloc[i]['xmin'])
        ymin = int(detections.iloc[i]['ymin'])
        xmax = int(detections.iloc[i]['xmax'])
        ymax = int(detections.iloc[i]['ymax'])
        label = detections.iloc[i]['name']
        confidence = detections.iloc[i]['confidence']

        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(frame, f'{label} {confidence:.2f}', (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Object Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()