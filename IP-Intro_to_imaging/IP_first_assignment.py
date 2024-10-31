import cv2 # for OpenCV
from skimage import io # for algorithms for image processing
import matplotlib.pylab as plt # for visualizations

# Load the image
url = "https://i1.sndcdn.com/avatars-Sm5TMJYaoC81wtFj-mJaIMQ-t240x240.jpg"
imRGB = io.imread(url) # reads in RGB
lenaImg = cv2.cvtColor(imRGB, cv2.COLOR_RGB2BGR)  # converts RGB to BGR

# Convert to grayscale
grayImg = cv2.cvtColor(lenaImg, cv2.COLOR_BGR2GRAY) # converts BGR to grayscale

# Extract the red channel, and make a new image with only the red channel
r = imRGB[:,:,0] # red channel

# Splitting the color channels to 3 different images
r, g, b = cv2.split(imRGB)

# Merging the color channels in a different order
imRGB_swapped = cv2.merge((g, b, r))

#DISPLAYING ALL IMAGES AT ONCE
# Create subplots, with 1 row and 3 columns. figsize is measured in inches
fig, axs = plt.subplots(1, 4, figsize=(15, 5))

# Display the original RGB image
axs[0].imshow(imRGB)
axs[0].set_title('Original RGB Image')
axs[0].axis('off')

# Display the grayscale image
axs[1].imshow(grayImg, cmap='gray')
axs[1].set_title('Grayscale Image')
axs[1].axis('off')

# Display the red channel image
axs[2].imshow(r, cmap='gray')
axs[2].set_title('Red Channel Image')
axs[2].axis('off')

# Display the swapped color channels image
axs[3].imshow(imRGB_swapped)
axs[3].set_title('Swapped Color Channels Image')
axs[3].axis('off')

# Show the plots
plt.show()