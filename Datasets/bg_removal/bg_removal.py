'''
Original Code by jedwards
Source: http://stackoverflow.com/questions/29313667/how-do-i-remove-the-background-from-this-kind-of-image
Note: This code has been modified to implement extra features
'''

'''
opencv issues: https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/zQjANEHPcJ0
'''

import cv2
import os #Moving files
import numpy as np

#== Parameters =======================================================================
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,1.0) # In BGR format


#== Processing =======================================================================

#-- Read image -----------------------------------------------------------------------
numImages = 2 # Total number of images to iterate through

for i in range(1, numImages + 1):
    print(i)
    img = cv2.imread('trees_to_remove_bg/tree' + str(i) + '.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #-- Edge detection -------------------------------------------------------------------
    edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    #-- Find contours in edges, sort by area ---------------------------------------------
    contour_info = []

    contours,_ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #Gives ValueError
    #See: http://stackoverflow.com/questions/25504964/opencv-python-valueerror-too-many-values-to-unpack
    #_, contours,_ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) Possible solution to ValueError

    for c in contours:
        contour_info.append((
            c,
            cv2.isContourConvex(c),
            cv2.contourArea(c),
        ))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
    max_contour = contour_info[0]

    #-- Create empty mask, draw filled polygon on it corresponding to largest contour ----
    # Mask is black, polygon is white
    mask = np.zeros(edges.shape)
    cv2.fillConvexPoly(mask, max_contour[0], (255))

    #-- Smooth mask, then blur it --------------------------------------------------------
    mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
    mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
    mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
    mask_stack = np.dstack([mask]*3)    # Create 3-channel alpha mask

    #-- Blend masked img into MASK_COLOR background --------------------------------------
    mask_stack  = mask_stack.astype('float32') / 255.0          # Use float matrices, 
    img         = img.astype('float32') / 255.0                 #  for easy blending

    masked = (mask_stack * img) + ((1-mask_stack) * MASK_COLOR) # Blend
    masked = (masked * 255).astype('uint8')                     # Convert back to 8-bit 

    cv2.imshow('img', masked)                                   # Display
    cv2.waitKey()

    #-- Check with user if bg was removed correctly -------------------------------------

    answer = str(raw_input('Was BG removal succesful? [y/n]: '))

    #If Yes, overwrite original image with masked image
    if(answer.lower() == 'y'):
        cv2.imwrite('/trees_to_remove_bg/tree' + str(i) + '.png', masked) # Save

    #If No, move original image to /failed folder
    else:
        os.rename('/trees_to_remove_bg/tree' + str(i) + '.png', '/trees_to_remove_bg/failed/tree' + str(i) + '.png')

    
