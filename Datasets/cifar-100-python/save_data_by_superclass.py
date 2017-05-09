'''
Description: Script to save into files the (1) array index of the images corresponding to an specific Superclass label name and
(2) the data of the images corresponding to said Superclass label name in the CIFAR-100 dataset. 

Command line argument: Superclass label name (i.e. trees, trucks, etc)

Author: Andres Vourakis

'''

import sys
import pickle
import numpy as np

def unpickle(file, enc):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding=enc)
    return dict

def get_label_index(labelName):
    # Get the label index corresponding to the Superclass (Coarse) label name

    i = None
    dict = unpickle('meta', 'ASCII')
    try:
        #i, = np.where(dict['label_names'] == labelName) #For numpy array only
        i = dict['coarse_label_names'].index(labelName) #For lists only
    except KeyError:
        print('The class label name does not exist. Check spelling or enter a different label name')
        
    return i

def save_train_images(labelName, label):
    #Find the indexes of the images corresponding to the label and save them into a text file
    
    pixels = []
    indexFileName = '{}_train_indexes_CIFAR_100.txt'.format(labelName)
    dataFileName = '{}_train_data_CIFAR_100.pickle'.format(labelName) #File to pickle

    with open(indexFileName, 'w') as indexFile, open(dataFileName, 'wb') as dataFile:
        dict = unpickle('train', 'bytes')
        for index, labelBatch in enumerate(dict[b'coarse_labels']):
            if labelBatch == label:
                indexFile.write(str(index) + '\n')
                pixels.append(dict[b'data'][index])
    
        pickle.dump(np.array(pixels), dataFile, protocol=2) # Pickle numpy array of pixels

def save_index_test_images(labelName, label):
    #Find the indexes of the images corresponding to the label and save them into a text file

    pixels = []
    indexFileName = '{}_test_indexes_CIFAR_100.txt'.format(labelName)
    dataFileName = '{}_test_data_CIFAR_100.pickle'.format(labelName)

    with open(indexFileName, 'w') as indexFile, open(dataFileName, 'wb') as dataFile:
        dict = unpickle('test', 'bytes')
        for index, labelBatch in enumerate(dict[b'coarse_labels']):
            if labelBatch == label:
                indexFile.write(str(index) + '\n')
                pixels.append(dict[b'data'][index])
    
        pickle.dump(np.array(pixels), dataFile, protocol=2) #Pickle numpy array of pixels

if __name__ == "__main__":

    labelName = sys.argv[1]
    label = get_label_index(labelName)
    save_train_images(labelName, label)
    save_index_test_images(labelName, label)


