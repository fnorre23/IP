import numpy as np                          # for ARRAYSs
import cv2 as cv                            # for OpenCV
# from google.colab.patches import cv2_imshow # for image display
from skimage import io                      # for algorithms for image processing
import matplotlib.pylab as plt              # provides a MATLAB-like interface
import copy                                 # help COPYing

url = "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png"
lenaImg = io.imread(url)
lenaImg = cv.cvtColor(lenaImg, cv.COLOR_RGB2BGR)
lenaImg = cv.resize(lenaImg,(256,256))
cv.imshow('Lena', lenaImg)

# THRESHOLD ##########################################################################
lenaGrey = cv.cvtColor(lenaImg, cv.COLOR_BGR2GRAY)
cv.imshow('Lena Grey', lenaGrey)
imageThreshold = copy.copy(lenaGrey)

# thresholding with loops

threshold = 150

for y in range(lenaGrey.shape[0]):
  for x in range(lenaGrey.shape[1]):
    if (lenaGrey[y,x]<threshold):
      imageThreshold[y,x] = 0
    else:
      imageThreshold[y,x] = 255

cv.imshow('Image thresholded', imageThreshold)

# thresholding with openCV function

ret,imageThreshold_2 = cv.threshold(lenaGrey,150,255,cv.THRESH_BINARY)
cv.imshow('Image thresholded 2', imageThreshold_2)

cv.waitKey(0)
cv.destroyAllWindows()

# 3x3 BOX ERODE ######################################################################

imErode = copy.copy(imageThreshold)

# erosion with loops

# Vi kan ændre ranges her til 2, -2, for at se bort fra borders
for y in range(1,imageThreshold.shape[0]-1):
  for x in range(1,imageThreshold.shape[1]-1):
    sum = 0
    # Range skal ændres til 5, da vores box er er så lang
    for ky in range (3):
      for kx in range (3):
        sum += imageThreshold[y+ky-1, x+kx-1]
    # Skal ganges med 25 fordi det passer med en 5x5 box 
    ######################### Hvis vi skal lave den til dilation, skal summen bare være større end 0 i princippet.
    if(sum == 255*9):
      imErode[y,x] = 255
    else:
      imErode[y,x] = 0

cv.imshow('Image thresholded', imageThreshold)
cv.imshow('Erode 3x3 LOOPS', imErode)

# erosion with OpenCV function cv.erode

kernel = np.ones((3,3), np.uint8) #define the kernel - needs to be uint8

imErode_2 = cv.erode(imageThreshold, kernel, iterations=1)
cv.imshow('Erode 3x3 OpenCV', imErode_2)


cv.waitKey(0)
cv.destroyAllWindows()

# 5x5 BOX ERODE #############################################################################

imErode = copy.copy(imageThreshold)

# erosion with loops

#DER SKAL PILLES VED DEN HER for at få 5x5 erode

# Vi kan ændre ranges her til 2, -2, for at se bort fra borders
for y in range(1,imageThreshold.shape[0]-1):
  for x in range(1,imageThreshold.shape[1]-1):
    sum = 0
    # Range skal ændres til 5, da vores box er er så lang
    for ky in range (5):
      for kx in range (5):
        sum += imageThreshold[y+ky-1, x+kx-1]
    # Skal ganges med 25 fordi det passer med en 5x5 box 
    ######################### Hvis vi skal lave den til dilation, skal summen bare være større end 0 i princippet.
    if(sum == 255*9):
      imErode[y,x] = 255
    else:
      imErode[y,x] = 0

cv.imshow('Image thresholded', imageThreshold)
cv.imshow('Erode 5x5 LOOPS',imErode)

# erosion with OpenCV function cv.erode

kernel = np.ones((3,3), np.uint8) #define the kernel - needs to be uint8

imErode_2 = cv.erode(imageThreshold, kernel, iterations=1)
cv.imshow('Erode 5x5 OpenCV', imErode_2)


cv.waitKey(0)
cv.destroyAllWindows()

# 3x3 DISK DILATE ##########################################################################

imDilate = copy.copy(imageThreshold)

kernel = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]])

# dilation with loops

for y in range(2,imageThreshold.shape[0]-2):
  for x in range(2,imageThreshold.shape[1]-2):
    sum = 0
    for ky in range (5):
      for kx in range (5):
        sum += imageThreshold[y+ky-2, x+kx-2] * kernel[ky,kx]
    if(sum >= 255):
      imDilate[y,x] = 255
    else:
      imDilate[y,x] = 0

cv.imshow('Image thresholded', imageThreshold)
cv.imshow('Dilation 3x3 Disk LOOPS',imDilate)

# dilation with OpenCV function dilate

kernel = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]],np.uint8)
#kernel needs to be uint8
imDilate_2 = cv.dilate(imageThreshold, kernel, iterations=1)
cv.imshow('Dilation 3x3 Disk OpenCV', imDilate_2)


cv.waitKey(0)
cv.destroyAllWindows()

# 5x5 DISK DILATE ############################################################################

imDilate = copy.copy(imageThreshold)

kernel = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]])

# dilation with loops

for y in range(2,imageThreshold.shape[0]-2):
  for x in range(2,imageThreshold.shape[1]-2):
    sum = 0
    for ky in range (5):
      for kx in range (5):
        sum += imageThreshold[y+ky-2, x+kx-2] * kernel[ky,kx]
    if(sum >= 255):
      imDilate[y,x] = 255
    else:
      imDilate[y,x] = 0

cv.imshow('Image thresholded', imageThreshold)
cv.imshow('Dilation 5x5 Disk LOOPS', imDilate)

# dilation with OpenCV function dilate

kernel = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]],np.uint8)
#kernel needs to be uint8
imDilate_2 = cv.dilate(imageThreshold, kernel, iterations=1)
cv.imshow('Dilation 5x5 Disk OpenCV', imDilate_2)

cv.waitKey(0)
cv.destroyAllWindows()