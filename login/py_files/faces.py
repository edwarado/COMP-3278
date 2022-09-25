import mysql.connector
import cv2
import pyttsx3
import pickle
from datetime import datetime
import os


def faces(username, password, type):
    count = 0
    # 1 Create database connection
    myconn = mysql.connector.connect(host="localhost",
                                     user=os.environ['user'],
                                     passwd=os.environ['passwd'],
                                     database=os.environ['database'])
    date = datetime.utcnow()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cursor = myconn.cursor()

    # 2 Load recognize and read label from model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("train.yml")

    labels = {"person_name": 1}
    with open("../../labels.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}

    # create text to speech
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 175)

    # Define camera and detect face
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    # 3 Open the camera and start face recognition
    while count < 400:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
        print(count)
        for (x, y, w, h) in faces:
            print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = recognizer.predict(roi_gray)

            # 3.1 If the face is recognized
            if conf <= 40:
                font = cv2.QT_FONT_NORMAL
                id = 0
                id += 1
                current_name = labels[id_]
                color = (255, 0, 0)
                stroke = 2
                cv2.putText(frame, labels[id_], (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                # Find the user's information in the database.
                if type == "CUSTOMER":
                    select = "SELECT * FROM CUSTOMER WHERE username=%s AND password=%s"
                else:
                    select = "SELECT * FROM ADMIN WHERE username=%s AND password=%s"
                name = cursor.execute(select, (username, password))
                result = cursor.fetchall()
                print(result)

                data = "error"
                for x in result:
                    data = x

                # If the user's information is not found in the database
                if data == "error":
                    print(current_name, "is NOT FOUND in the database.")
                    cap.release()
                    cv2.destroyAllWindows()
                    return 0

                # If the user's information is found in the database
                else:
                    if type == "CUSTOMER":
                        select = "SELECT * FROM CUSTOMER WHERE username=%s AND password=%s"
                    else:
                        select = "SELECT * FROM ADMIN WHERE username=%s AND password=%s"

                    name = cursor.execute(select, (username, password))
                    result = cursor.fetchall()
                    print(current_name, result)

                    data = "error"
                    for res in result:
                        data = res
                    if data == "error":
                        # not found
                        return 0

                    # update last login
                    if type == "CUSTOMER":
                        select = "SELECT login_id, login_time, login_date FROM CUSTOMER_LOGIN_HISTORY  WHERE username=%s"
                        cursor.execute(select, (username,))
                        result = cursor.fetchall()
                        data = "error"
                        for res in result:
                            data = res
                        if data != "error":
                            (_, time, date) = data
                            update = "UPDATE CUSTOMER SET last_login_time=%s,last_login_date=%s WHERE username=%s"
                            cursor.execute(update, (time, date, current_name))
                            myconn.commit()
                    else:
                        select = "SELECT MAX(login_id), login_time, login_date FROM ADMIN_LOGIN_HISTORY WHERE username=%s"
                        cursor.execute(select, (username,))
                        result = cursor.fetchall()
                        data = "error"
                        for res in result:
                            data = res
                        if data != "error":
                            (_, time, date) = data
                            update = "UPDATE ADMIN SET last_login_time=%s,last_login_date=%s WHERE username=%s"
                            cursor.execute(update, (time, date, current_name))
                            myconn.commit()

                    # update login info

                    if type == "CUSTOMER":
                        count = "SELECT COUNT(*) FROM CUSTOMER_LOGIN_HISTORY"
                    else:
                        count = "SELECT COUNT(*) FROM ADMIN_LOGIN_HISTORY"

                    name = cursor.execute(count)
                    result = cursor.fetchall()
                    maxID = result[0][0]
                    print(maxID)

                    if type == "CUSTOMER":
                        insert = "INSERT INTO CUSTOMER_LOGIN_HISTORY VALUES (%s, %s, %s, %s)"
                    else:
                        insert = "INSERT INTO ADMIN_LOGIN_HISTORY VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert, (maxID + 1,
                                            current_name,
                                            datetime.utcnow(),
                                            datetime.now().strftime("%H:%M:%S")))
                    myconn.commit()

                    cap.release()
                    cv2.destroyAllWindows()

                    return 1

                    # hello = ("Hello ", current_name, "Welcome to the iKYC System")
                    # print(hello)
                    # engine.say(hello)
                    # engine.runAndWait()

            # 3.2 If the face is unrecognized
            else:
                color = (255, 0, 0)
                stroke = 2
                font = cv2.QT_FONT_NORMAL
                cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                hello = ("Your face is not recognized")
                print(hello)
                engine.say(hello)
                # engine.runAndWait()

        count += 1
        cv2.imshow('iKYC System', frame)
        k = cv2.waitKey(20) & 0xff
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return -1
