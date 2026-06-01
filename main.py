import cv2
import mediapipe as mp
import numpy as np
import time
import pygame

# MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Camera
cap = cv2.VideoCapture(0)

# Eye landmarks
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Settings
EAR_THRESHOLD = 0.20
CLOSED_TIME_LIMIT = 3

closed_start_time = None
alarm_on = False

# Alarm sound
pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")


def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def eye_aspect_ratio(points):
    p1, p2, p3, p4, p5, p6 = points

    vertical1 = distance(p2, p6)
    vertical2 = distance(p3, p5)
    horizontal = distance(p1, p4)

    ear = (vertical1 + vertical2) / (2.0 * horizontal)

    return ear


while True:
    success, frame = cap.read()

    if not success:
        print("Camera not found")
        break

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]

        left_points = []
        right_points = []

        for idx in LEFT_EYE:
            x = int(face_landmarks.landmark[idx].x * w)
            y = int(face_landmarks.landmark[idx].y * h)
            left_points.append((x, y))
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

        for idx in RIGHT_EYE:
            x = int(face_landmarks.landmark[idx].x * w)
            y = int(face_landmarks.landmark[idx].y * h)
            right_points.append((x, y))
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

        left_ear = eye_aspect_ratio(left_points)
        right_ear = eye_aspect_ratio(right_points)

        avg_ear = (left_ear + right_ear) / 2.0

        if avg_ear < EAR_THRESHOLD:
            status = "EYES CLOSED"
            color = (0, 0, 255)

            if closed_start_time is None:
                closed_start_time = time.time()

            closed_duration = time.time() - closed_start_time

            cv2.putText(
                frame,
                f"Closed Time: {closed_duration:.1f}s",
                (20, 130),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            if closed_duration >= CLOSED_TIME_LIMIT:
                status = "DROWSINESS ALERT!"

                if not alarm_on:
                    pygame.mixer.music.play(-1)
                    alarm_on = True

        else:
            status = "EYES OPEN"
            color = (0, 255, 0)

            closed_start_time = None

            if alarm_on:
                pygame.mixer.music.stop()
                alarm_on = False

        cv2.putText(
            frame,
            status,
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

        cv2.putText(
            frame,
            f"EAR: {avg_ear:.2f}",
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            
        )

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()