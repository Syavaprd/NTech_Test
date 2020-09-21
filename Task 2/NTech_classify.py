
from keras.models import load_model
from os import listdir
from os.path import join, dirname, abspath, isfile
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
import numpy as np
import json

image_size = 260

def classify(path_to_model, test_img_dir):
    x=[]
    result = {}
    model = load_model(path_to_model)
    onlyfiles = [f for f in listdir(test_img_dir) if isfile(join(test_img_dir, f))]              # get only files from input directory

    for fname in onlyfiles:
        img = image.load_img(join(test_img_dir,fname), target_size=(image_size, image_size))
        img = image.img_to_array(img)
        img = preprocess_input(img)
        img = np.expand_dims(img, 0)
        y_prob = model.predict(img, batch_size=1)
        if y_prob[0][0] >= 0.5:
            result[fname] = 'male'
        else:
            result[fname] = 'female'
    
    with open('./process_results.json', 'w') as fp:                                            #save dict as json
        json.dump(result, fp)

if __name__ == '__main__':
    if len(argv) != 3:
        raise NameError('Small amount of arguments\n')
    model_path = argv[1]
    image_path = argv[2]
    classify(model_path, image_path)
