
from PIL import Image
from numpy import array
#from colorMap import ColorMap
from keymap import ColorMap

#####################################################################
# http://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green
#####################################################################
import webcolors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in ColorMap.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]
'''
# Example
requested_colour = (119, 172, 152)
closest_name = closest_colour(requested_colour)
print "closest colour name:", closest_name
'''
#####################################################################
#####################################################################
#####################################################################


'''
Return a layout of a tree in a 2D array
'''

def image_to_array(fileName):
        img = Image.open(fileName)
	arr = array(img)
	return arr

def array_to_image(array):
	img = Image.fromarray(arr)
	return img

counter = 0 
asdf = ['trees/tt1.png','trees/tt2.png','trees/tt3.png','trees/tt4.png','trees/tt5.png',
	'trees/tt6.png']


def get_next_image():
    global counter
    arr = image_to_array(asdf[counter])
    counter+=1
    if counter == 6:
        counter = 0
    return arr

def getNextLayout():
    image = get_next_image()
    
    full_layout = []
    
    for i in range(len(image)):
        row = []
        for j in range(len(image[i])):
            color = closest_colour(image[i][j])
            row.append(color)
        full_layout.append(row)
    return full_layout
    ''' Layout EXAMPLE
    layout1 = [['GREEN', 'GREEN', 'GREEN','GREEN','GREEN'],
                  ['', '', 'BROWN','',''],
                  ['', '', 'BROWN','',''],
                  ['', '', 'BROWN','','']
                 ]
    '''



