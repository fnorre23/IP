import cv2
import copy
import numpy as np

# Grassfire function - taking an x-value of pixel, y-value of pixel, a label, and an image 
def grassFireS(y,x,label,im):

  # Initialize lists to contain x and y values
  Ylist = []
  Xlist = []

  # Add initial pixel to the list
  Ylist.append(y)
  Xlist.append(x)

  # Assign the initial pixel the label
  im[y,x] = label

  # Grassfire loop
  while(len(Ylist)>0):

    # Pop the first element from the list and assign it to y and x
    y = Ylist.pop(0)
    x = Xlist.pop(0)

    # Check if the pixel above is white, and if so, assign the label to it and append it to the list
    if (y>0 and im[y-1,x] == 255):

      # Assign the label to the pixel
      im[y-1,x] = label

      # Append the new pixel to the list
      Ylist.append(y-1)
      Xlist.append(x)

    # Check pixel below - same procedure
    if (y<im.shape[0]-1 and im[y+1,x] == 255):
      im[y+1,x] = label
      Ylist.append(y+1)
      Xlist.append(x)

    # Check pixel to the left - same procedure
    if (x>0 and im[y,x-1] == 255):
      im[y,x-1] = label
      Ylist.append(y)
      Xlist.append(x-1)


    # Check pixel to the right - same procedure
    if (x<im.shape[1]-1 and im[y,x+1] == 255):
      im[y,x+1] = label
      Ylist.append(y)
      Xlist.append(x+1)

# Reading image, in inverting to get correct binary
img = cv2.imread("test.png") 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY_INV)

imlabel = copy.copy(img)

label = 50  # label assigned to each pixel within a blob. In this case the label is a brightness value
total_blobs = 0 # Blob counter

# Scanning the image, and applying grassfire method when it finds a white pixel.
for y in range(imlabel.shape[0]):
  for x in range(imlabel.shape[1]):
    if (imlabel[y,x] == 255):
      grassFireS(y,x,label,imlabel) # Apply label to first found shape and all pixels in it
      label += 25  # Add more intensity to label, so next shape is 25 values brighter.
      total_blobs += 1 # Adding a new blob to the blob counter

# Calculating areas for all blobs #################################

area = copy.copy(imlabel) # Make new array to get areas of blobs.

# Creating a list the length of labels (which is way too long), and 
areaArray = [0]*label
for x in range (area.shape[0]):
  for y in range (area.shape[1]):
   for i in range (1,label):
      if (area[x,y] == i):
        areaArray[i] +=1

# Making new array with all values that are not 0 - aka all the shapes areas
areaArray_noZeros = [value for value in areaArray if value > 0] # This looks at all values from areaArray, and adds it if the value is above 0

# Sort by size, low to big
areaArray_noZeros = np.sort(areaArray_noZeros)

# Call the last index - aka biggest number
biggest_blob_area = areaArray_noZeros[-1]

# Getting label index
biggest_blob_label = areaArray.index(biggest_blob_area)

## SOLUTION 1 ###############################################################

# Making copy for solution 1
solution_1 = copy.copy(imlabel)

# Modifying the image, to only show pixels with the label corresponding to the biggest shape
for x in range(solution_1.shape[0]):
  for y in range(solution_1.shape[1]):
    if solution_1[x, y] == biggest_blob_label:
      solution_1[x, y] = 255
    else:
      solution_1[x, y] = 0

## SOLUTION 2 (Help to simplify code from copilot) ###########################

# Making copy for solution 2
solution_2 = copy.copy(imlabel)

# Alternate numpy method
solution_2 = np.where(solution_2 == biggest_blob_label, 255, 0).astype(np.uint8) 

# This returns an array where if condition is met, it applies 1 value, if not, it applies the other.
# .astype(np.uint8) converts the array to an the correct type to be able to show it through cv2.imshow

cv2.imshow("Solution 1", solution_1)
cv2.imshow("Solution 2", solution_2)
cv2.waitKey(0)
cv2.destroyAllWindows

#TODO 3rd solution - Erosion + Dilation method?
