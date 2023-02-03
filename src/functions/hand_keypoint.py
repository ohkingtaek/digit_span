import cv2
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


def detect_hand_keypoints(width, height, frame):
    temp = None
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
 
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            normalizedLandmark = hand_landmarks.landmark[8]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, width, height
            )

            print(pixelCoordinatesLandmark)
            temp = pixelCoordinatesLandmark
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return temp, frame
