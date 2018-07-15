import cv2

img= cv2.imread( 'picaso.jpg' )
imgGray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
(thresh, im_bw) = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
im_bw = cv2.threshold(imgGray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow( "original", img )
cv2.imshow( "Resultado", im_bw )    
cv2.waitKey(0)
cv2.destroyAllWindows()
