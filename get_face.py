# Mehmet Alp Aysan

import cv2
import numpy as np
import pyimgur

CLIENT_ID = "100ef2fd6ae00e0"


def get_url_string():
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image("Face1.png", title="Image for Face ID")
    return uploaded_image.link


def get_face():

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    if face_cascade.empty(): raise Exception("your face_cascade is empty. are you sure, the path is correct ?")

    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    if eye_cascade.empty(): raise Exception("your eye_cascade is empty. are you sure, the path is correct ?")

    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    time = 0

    while vc.isOpened():
        ret, frame = vc.read()
        if frame is None:
            break

        print(time)
        if time == 10:
            cv2.imwrite("Face1.png", frame)
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if(len(faces) != 0):
            time += 1
        else:
            time = 0

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow('preview', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vc.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    get_face()
