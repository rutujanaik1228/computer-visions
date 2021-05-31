import cv2
img=cv2.imread("rutuja.jpeg",0)
print(img)#0-255 range
cv2.imshow("image",img)  #shows imgae
cv2.waitKey()            #pause image
cv2.destroyAllWindows()  #distroy the windows that was opened
