import cv2
import dlib
import numpy as np
import os

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("..\..\shape_predictor_68_face_landmarks.dat")
cap = cv2.VideoCapture(0)
mood = input("Enter your mood:")
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(frame)
    
    for face in faces:
        landmarks = predictor(frame,face)
        #print(landmarks.parts())
        nose = landmarks.parts()[28]
        #print(nose.x, nose.y)
        lip_up = landmarks.parts()[62].y
        lip_down = landmarks.parts()[66].y

        if lip_down - lip_up>5:
            print("open")
        else:
            print("closed")
        expression = np.array([[point.x - face.left(), point.y-face.top()] for point in landmarks.parts()[17:]])
        print(expression.flatten())

    
    if ret:

        cv2.imshow("My Screen", frame)
        
    
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

    elif key == ord("c"):
        #cv2.imwrite(name + ".jpg", frame)
        frames.append(gray.flatten())
        outputs.append([mood])
X = np.array(frames)
y = np.array(outputs)

data = np.hstack([y, X])

f_name = "face_mood.npy"

if os.path.exists(f_name):
    old = np.load(f_name)
    data = np.vstasck([old,data])

np.save(f_name,data)
cap.release()
cv2.destroyAllWindows()
