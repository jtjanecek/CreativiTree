from PIL import Image
import pickle
import numpy as np


with open('trees_train_data_CIFAR_100.pickle', 'rb') as file:
    for data in pickle.load(file):
        img = Image.fromarray(data, 'RGB')
        img.save('my.png')
        img.show()
    
    
