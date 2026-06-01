# AI-Based Driver Drowsiness Detection System

## Overview

This project is a real-time Driver Drowsiness Detection System developed using Python, OpenCV, MediaPipe Face Mesh, NumPy, and Pygame.

The system monitors a driver's eyes through a webcam, calculates the Eye Aspect Ratio (EAR), detects prolonged eye closure, and triggers an alarm when drowsiness is detected.

## Features

* Real-time face detection
* Eye landmark detection using MediaPipe Face Mesh
* Eye Aspect Ratio (EAR) calculation
* Eye Open / Eye Closed detection
* Drowsiness detection based on eye closure duration
* Alarm notification system
* Real-time status monitoring

## Technologies Used

* Python
* OpenCV
* MediaPipe Face Mesh
* NumPy
* Pygame

## Project Structure

DriverDrowsinessAI/

├── main.py

├── alarm.mp3

├── requirements.txt

└── README.md

## System Workflow

1. Capture live video from the webcam.
2. Detect the driver's face using MediaPipe Face Mesh.
3. Extract eye landmarks from the detected face.
4. Calculate the Eye Aspect Ratio (EAR).
5. Determine whether the eyes are open or closed.
6. Start a timer when eyes remain closed.
7. Trigger a drowsiness alert if eyes stay closed for more than 3 seconds.
8. Play an alarm sound until the driver's eyes reopen.

## Eye Aspect Ratio (EAR)

The system uses the Eye Aspect Ratio (EAR) to determine eye state.

* EAR > 0.20 → Eyes Open
* EAR < 0.20 → Eyes Closed

If the eyes remain closed continuously for more than 3 seconds, the system identifies the driver as drowsy and activates an alert.

## Installation

Clone the repository:

```bash
git clone https://github.com/navishd/DriverDrowsinessAI.git
cd DriverDrowsinessAI
```

Create a virtual environment:

```bash
python3.11 -m venv venv311
```

Activate the environment:

```bash
source venv311/bin/activate
```

Install dependencies:

```bash
pip install opencv-python mediapipe numpy pygame
```

## Run the Project

```bash
python main.py
```

## Expected Output

### Normal State

* Face detected
* Eyes open
* Driver status displayed as safe

### Drowsiness State

* Eyes remain closed for more than 3 seconds
* DROWSINESS ALERT message displayed
* Alarm sound activated

## Applications

* Driver safety monitoring
* Transportation systems
* Smart vehicle assistance
* Fleet management systems
* Accident prevention systems

## Future Improvements

* Yawn Detection
* Head Pose Estimation
* Mobile Phone Usage Detection
* Driver Attention Monitoring
* AI Dashboard and Analytics
* Cloud-Based Monitoring System

## License

This project is developed for educational and research purposes.
