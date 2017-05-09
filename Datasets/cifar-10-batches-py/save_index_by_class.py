'''
Description: Script to save into a file the array index of the images corresponding to an specific class label in the CIFAR-10 dataset.
These indexes can then be used to iterate over a desired class of images (i.e. bird, ship, etc...)

Author: Andres Vourakis

'''

import sys
import numpy as np

def unpickle(file, enc):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding=enc)
    return dict

'''
def print_batches_meta(dict):
    #Print label names
    for index, name in enumerate(dict['label_names']):
        print("{}: {}".format(index, name))

def print_batches(dict):
    #Print labels with file names
    for index, label in enumerate(dict[b'labels']):
        print("{}: {}\n".format(label, dict[b'filenames'][index]))

    print('Size of batch: {}\n'.format(len(dict[b'labels'])))
'''

def get_label_index(labelName):
    # Get the label index corresponding to the class label name

    i = None
    dict = unpickle('batches.meta', 'ASCII')
    try:
        #i, = np.where(dict['label_names'] == labelName) #For numpy array only
        i = dict['label_names'].index(labelName) #For lists only
    except KeyError:
        print('The class label name does not exist. Check spelling or enter a different label name')
        
    return i

def save_index_train_images(labelName, label):
    #Find the indexes of the images corresponding to the label and save them into a text file

    outputFileName = '{}_train_indexes_CIFAR_10.txt'.format(labelName)
    totalBatchFiles = 5

    with open(outputFileName, 'w') as file:
        counter = 1
        while(counter != totalBatchFiles):
            inputFileName = 'data_batch_{}'.format(counter)
            for index, labelBatch in enumerate(unpickle(inputFileName, 'bytes')[b'labels']):
                if labelBatch == label:
                    file.write(str(index) + '\n')
            counter +=1

def save_index_test_images(labelName, label):
    #Find the indexes of the images corresponding to the label and save them into a text file

    outputFileName = '{}_test_indexes_CIFAR_10.txt'.format(labelName)

    with open(outputFileName, 'w') as file:
        for index, labelBatch in enumerate(unpickle('test_batch', 'bytes')[b'labels']):
            if labelBatch == label:
                file.write(str(index) + '\n')


if __name__ == "__main__":
    #Takes class labelname as command line argument

    labelName = sys.argv[1]
    label = get_label_index(labelName)
    save_index_train_images(labelName, label)
    save_index_test_images(labelName, label)


