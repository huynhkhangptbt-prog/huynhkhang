import os

os.environ["TF_USE_LEGACY_KERAS"] = "1"

import cv2
import numpy as np
from tensorflow.keras.models import load_model




MODEL_PATH = r"/model/keras_model.h5"
LABELS_PATH = r"/model/labels.txt"




print("Đang tải model...")

model = load_model(
    MODEL_PATH,
    compile=False
)

print("Đã tải model thành công!")




with open(
    LABELS_PATH,
    "r",
    encoding="utf-8"
) as f:
    class_names = f.readlines()

print("Labels:", [x.strip() for x in class_names])




camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Không thể mở camera!")
    exit()

print("Camera đã mở.")
print("Nhấn ESC để thoát.")


while True:

    ret, frame = camera.read()

    if not ret:
        print("Không thể đọc camera!")
        break


    display_image = frame.copy()


    image = cv2.resize(
        frame,
        (224, 224),
        interpolation=cv2.INTER_AREA
    )


    image = np.asarray(
        image,
        dtype=np.float32
    )

    image = image.reshape(
        1, 224, 224, 3
    )


    image = (image / 127.5) - 1




    prediction = model.predict(
        image,
        verbose=0
    )

    index = np.argmax(prediction[0])

    class_name = class_names[index].strip()

    confidence = float(
        prediction[0][index]
    )



    text = f"{class_name}: {confidence * 100:.1f}%"

    cv2.putText(
        display_image,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )


    cv2.imshow(
        "AI Camera",
        display_image
    )


    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break


camera.release()
cv2.destroyAllWindows()

print("Đã thoát chương trình.")
