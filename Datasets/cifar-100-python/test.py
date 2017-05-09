import pickle

def unpickle(file, enc):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding=enc)
    return dict


if __name__ == '__main__':
    file = unpickle('trees_train_data_CIFAR_100.pickle', 'bytes')
    for i in file:
        print(len(i))
        print(i)
