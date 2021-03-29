import cv2
import numpy as np
import keyboard

cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('test.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (380,380))
j=0
while(cap.isOpened()):
    ret, img = cap.read()
    y,h,x,w=50,380,130,380
    img2 = img[y:y+h, x:x+w]
    #blur = cv2.GaussianBlur(img,(1,1),0)
    imgYCC = cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)
    lower = np.array([58, 54, 78]) #[58,135,114]
    upper = np.array([255, 153, 132])
    imgMASK = cv2.inRange(imgYCC, lower, upper)
    imgMASK2 = imgMASK.copy()
    contours,_=cv2.findContours(imgMASK, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    New_contours=[]
    for i in range(len(contours)):
        cnt=contours[i]
        epsilon=0.0003*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        hull = cv2.convexHull(cnt)
        New_contours.append(hull)
    img = cv2.drawContours(imgMASK,New_contours, -1, (255,255,0),3)
    # Show some stuff
    cv2.imshow("image",imgYCC)
    cv2.imshow("imgMASK",imgMASK2)
    cv2.imshow("Contours", img)
    # Wait until user press some key
    c = cv2.waitKey(25) 
    if keyboard.read_key() == "w":
      nom = 'caca_{}.png'.format(j)
      cv2.imwrite(nom,imgMASK2)
      j+=1

    
out.release()
cv2.destroyAllWindows()