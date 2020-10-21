import os
import pickle

import cv2
import numpy as np
from PIL import Image

from Login.settings import MEDIA_ROOT, BASE_DIR


image_dir = MEDIA_ROOT
face_dir = os.path.join(BASE_DIR, 'cascades\haarcascade_frontalface_alt2.xml')
face_cascade = cv2.CascadeClassifier(face_dir)
recognizer = cv2.face.LBPHFaceRecognizer_create()
train_dir = os.path.join(BASE_DIR,'trainer\\trainer.yml')
def train():
    face_samples = []
    ids = {}
    labels =[]
    current_id = 1

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith('png') or file.endswith('jpg') or file.endswith('jpeg'):
                path = os.path.join(root, file)
                label = os.path.basename(os.path.dirname(path))
                print(label)
                if not label in ids:
                    ids[label] = current_id
                    current_id += 1

                print(ids)

                pil_image = Image.open(path).convert("L")  # it converts the image into grayscale
                #size = (400,400)
                #final_image = pil_image.resize(size,Image.ANTIALIAS)
                idf = ids[label]
                image_array = np.array(pil_image, "uint8")  # we are going to train the image on this numpy array
                print(image_array)
                faces = face_cascade.detectMultiScale(image_array)
                for (x, y, w, h) in faces:
                    face_samples.append(image_array[y:y + h, x:x + w])
                    labels.append(idf)

    with open("label.pickle", "wb") as file:
        pickle.dump(ids, file)
        file.close()
    recognizer.train(face_samples, np.array(labels))
    recognizer.write(train_dir)
    print('trained')
