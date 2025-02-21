import cv2
import face_recognition
import numpy as np
import os

DATASET_PATH = "face_data/"

def recognize_face():
    known_faces = {}
    for file in os.listdir(DATASET_PATH):
        name = file.replace(".npy", "")
        known_faces[name] = np.load(os.path.join(DATASET_PATH, file))

    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_encodings = face_recognition.face_encodings(rgb_frame)
        for face_encoding in face_encodings:
            matches = {name: face_recognition.compare_faces([enc], face_encoding)[0] 
                       for name, enc in known_faces.items()}

            for name, match in matches.items():
                if match:
                    print(f"Access Granted: {name}")
                    cam.release()
                    cv2.destroyAllWindows()
                    return name

        cv2.imshow("Face Recognition - Press 'q' to Quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    return None
