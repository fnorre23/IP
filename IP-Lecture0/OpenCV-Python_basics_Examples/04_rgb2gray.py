#import the required libraries 
import numpy as np 
import cv2 

image = cv2.imread('lena_colored.jpg', cv2.IMREAD_COLOR) 
#converting image to Gray scale 
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#plotting the grayscale image
cv2.imshow('image',gray_image) 

cv2.waitKey(0)
cv2.destroyAllWindows()