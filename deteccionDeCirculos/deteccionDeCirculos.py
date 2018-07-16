import cv2
import numpy as np

img= cv2.imread( 'circulos.jpg' )
imgGray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )

th, im_th = cv2.threshold(imgGray, 180, 255, cv2.THRESH_BINARY_INV)
 
# Copy the thresholded image.
im_floodfill = im_th.copy()
 
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255)
 
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)



cv2.imshow( "original", img )
cv2.imshow("Thresholded Image", im_th)
cv2.imshow("Floodfilled Image", im_floodfill)
cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
