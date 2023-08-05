import cv2
import joblib
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import cv2


def is_cracked(image_path):
    img = image.load_img(image_path, target_size=(128, 128))

    img1 = image.img_to_array(img)
    img1 = img1 / 255

    img1 = np.expand_dims(img1, [0])

    # Load the model from the file
    model = joblib.load('model.pkl')
    result = model.predict(img1)

    if result[0] >= 0.5:
        return "Crack Detected"
    else:
        return "No Crack Detected"

# for testing
# is_cracked("surface_crack_detection/Positive/00005.jpg")
