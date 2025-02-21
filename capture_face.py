import cv2
import face_recognition
import numpy as np
import os

DATASET_PATH = "face_data/"
os.makedirs(DATASET_PATH, exist_ok=True)

def capture_face(name):
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv2.imshow("Capture Face - Press 's' to Save", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            face_encodings = face_recognition.face_encodings(frame)
            if face_encodings:
                np.save(f"{DATASET_PATH}{name}.npy", face_encodings[0])
                print(f"Face data saved for {name}")
                break
            else:
                print("No face detected. Try again.")

    cam.release()
    cv2.destroyAllWindows()
