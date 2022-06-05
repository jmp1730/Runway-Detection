from tensorflow.keras.models import model_from_json
import numpy as np
import cv2
import pickle

class Model(object):
    
    def __init__(self, model_json_file, model_weights_file):
        # load model from JSON file
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)
            

        # load weights into the new model
        self.loaded_model.load_weights(model_weights_file)
        print("Model loaded from disk")
        self.loaded_model.summary()
        # pickle_out = open("le.pickle","rb")
        # self.le=pickle.load(pickle_out)
        
        
        

    def predict_(self, img):
        self.preds = self.loaded_model.predict(img)[0]
        print(self.preds)
        pred=np.argmax(self.preds)
        
        
        print(pred)
        if pred==34:
            return 1
        else: return 0    
        return self.preds

from PIL import Image
from PIL import ImageFilter
def delayed_insert(label,index,message):
    label.insert(index,message) 

def prediction(path,lb1):
    lb1.after(1,delayed_insert,lb1,0,"Starting runway detection")
    lb1.after(10,delayed_insert,lb1,1,"Loading model")
    
    model=Model('model2.json','model2.h5')
    lb1.after(30,delayed_insert,lb1,2,"Reading image")
    img=cv2.imread(path)
    
    lb1.after(100,delayed_insert,lb1,3,"Resizing image")
    
    img=cv2.resize(img,(224,224))
    img=np.reshape(img,(1,224,224,3))
    lb1.after(130,delayed_insert,lb1,4,"Detection")
    pred=model.predict_([img])
    print(pred)
    if pred==1:
        msg="Runway detected"
    else:
        msg="Runway not detected"    
    lb1.after(230,delayed_insert,lb1,5,msg)
    return pred


if __name__ == '__main__':
    model=Model('model2.json','model2.h5')
    img=cv2.imread('NWPU-RESISC45/runway/runway_500.jpg')

    img=cv2.resize(img,(224,224))
    img=np.reshape(img,(1,224,224,3))
    pred=model.predict_([img])
    print(pred)

