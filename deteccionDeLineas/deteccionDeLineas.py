import cv2
import numpy as np
def canny(image, sigma=0.33):
	v = np.median(image)
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edges = cv2.Canny(image, lower, upper)
	return edges

img= cv2.imread( 'mar.jpg' )
imgGray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
cv2.imshow( "original", img )
cv2.imshow( "Resultado", canny(imgGray) )
cv2.waitKey(0)
cv2.destroyAllWindows()