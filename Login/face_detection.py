import pickle
import cv2


def verify():
    from Login.trainit import face_dir, train_dir
    # face cascade
    predicted_name = "unknown"

    face_cascade = cv2.CascadeClassifier(face_dir)
    # initialize recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # read trained data
    recognizer.read(train_dir)
    with open("label.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}
    # initialize camera
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    userId = 0
    while True:
        ret, frame = cam.read()
        # convert into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(int(minW), int(minH)))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            label, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            predicted_name = labels[label]
            print(label)
            print(confidence)

            if confidence> 0:
                userId = label
                confidence = 100 - round(confidence)
                cv2.putText(frame, 'Detected' + predicted_name, (x + 2, y + h - 4), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (150, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        cv2.imshow('Face Recognizer', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    return predicted_name