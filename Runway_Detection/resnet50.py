from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten,Dropout
import tensorflow as tf
tf.compat.v1.reset_default_graph()

def build_model():
    # load model without classifier layers
    model = ResNet50(include_top=False, input_shape=(150, 150, 3),weights='imagenet')

    # mark loaded layers as not trainable
    for layer in model.layers:
        layer.trainable = False
    # add new classifier layers
    flat1 = Flatten()(model.layers[-1].output)
    class1 = Dense(1024, activation='relu')(flat1)
    class2 = Dense(512, activation='relu')(class1)

    output = Dense(36, activation='softmax')(class2)
    # define new model
    model = Model(inputs=model.inputs, outputs=output)
    # summarize
    model.summary()
    return model

if __name__=='__main__':
    build_model()    