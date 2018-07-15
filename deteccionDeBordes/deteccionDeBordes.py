import os
import cv2
import numpy as np
def canny(image, sigma=0.33):
	v = np.median(image)
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edges = cv2.Canny(image, lower, upper)
	return edges
def sobel(img):
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    cv2.imshow( "sobel x", sobelx )
    return sobely
def menu(opciones, texto=''):
    opcion = -100
    while(opcion < 0 or opcion > len(opciones)):
        while True:
            print('\t Menu Selecione una opcion')    
            print(texto)
            for i, x in enumerate(opciones):
                print(str(i+1)+ "-. "+ str(x))
            try:
                opcion = int(input("ingrese una opcion valida: "))
                break
            except ValueError:
                os.system ("cls")
                print("ingrese una opcion valida")
    return opcion
def prewiit(img):
    img_gaussian = cv2.GaussianBlur(img,(3,3),0)
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
    cv2.imshow( "Prewitty x", img_prewittx )
    return img_prewitty
opcion = menu(['Canny','Sobel','Prewiit'])

img = cv2.imread( 'mty.jpg' )
imgGray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
result = {
        1: canny(imgGray, .1),
        2: sobel(imgGray),
        3: prewiit(imgGray)
    }.get(opcion,1)


cv2.imshow( "original", img )
cv2.imshow( "grey.png", imgGray )
cv2.imshow( "resultado", result )
cv2.waitKey(0)
cv2.destroyAllWindows()
