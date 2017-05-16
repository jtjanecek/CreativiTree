
'''
Basic script to download images given urls in a file
'''

from tqdm import tqdm
import mmap
import urllib.request

chunk_size = 1024

inputFile = 'trees.imagenet.synset.geturls'
failedFile = 'failed_urls.txt'

def get_line_number(fileName):
    '''
    Source: http://blog.nelsonliu.me/2016/07/30/progress-bars-for-python-file-reading-with-tqdm/
    '''
    with open(fileName, 'r+') as file:
        buf = mmap.mmap(file.fileno(), 0)
        lines = 0
        while buf.readline():
            lines += 1
        return lines

with open(inputFile, 'r') as data, open(failedFile, 'w') as log:
    counter = 1;
    for url in tqdm(data, total=get_line_number(inputFile)):
        try:
            fileName = './tree_images/tree' + str(counter) + '.png'
            urllib.request.urlretrieve(url, fileName)
            counter += 1
        except:
            log.write(url)
            
