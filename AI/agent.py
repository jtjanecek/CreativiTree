
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
asdf = {0:'trees/tt1.png',1:'trees/tt2.png',2:'trees/tt3.png', 3:'trees/tt4.png',4:'trees/tt5.png'}

def get_next_image():
    global counter
    arr = image_to_array(asdf[counter])
    counter+=1
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

    layout1 = [['GREEN', 'GREEN', 'GREEN','GREEN','GREEN'],
                  ['', '', 'BROWN','',''],
                  ['', '', 'BROWN','',''],
                  ['', '', 'BROWN','','']
                 ]  
    return layout1



f = open('keymap.txt','w')
for key, name in webcolors.css3_hex_to_names.items():
	f.write('ColorMap[' + key + '] = ' + "'" + name + "'" + '\n')	
f.close()

