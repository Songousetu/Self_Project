# -*- coding: utf-8 -*-
import os
import time
import json
import redis
import base64
import traceback
from PIL import Image
import json
from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input
import cv2
import numpy as np
from keras.models import load_model


def predict(model, img_path):
    # img = cv2.imread(img_path)
    # img = cv2.cvtColor(img)


    img = Image.open(img_path)
    target_size = (229, 229)
    if img.size != target_size:
        img = img.resize(target_size)

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)


    preds = model.predict(x)

    tempJson = {}
    for i in range(len(preds[0])):
        temp = {}
        key = i + 1
        value = round(float(preds[0][i]),5)
        temp[key] = value
        tempJson.update(temp)
        output = tempJson

    return output


if __name__ == '__main__':
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"  # see issue #152
    os.environ['CUDA_VISIBLE_DEVICES'] = "0"
    redis_client = redis.StrictRedis(host='160.46.82.236', port=6379, db=0, password='nsmi#pw2018')
    model = load_model('/home/nsm/trunk/workshop/ws/my_model.h5')

    while True:
        try:
            image = redis_client.rpop('images_queue')
            if image is not None:
                data = json.loads(image.decode("utf-8"))
                id = data['id']
                image = base64.b64decode(data['image'])
                image_path = os.path.join('images', id)

                with open(image_path, 'wb') as f:
                    f.write(image)
                output = predict(model, image_path)
                redis_client.set(id, json.dumps(output))
                continue
            time.sleep(0.01)
        except Exception as e:
            print(traceback.print_exc())
