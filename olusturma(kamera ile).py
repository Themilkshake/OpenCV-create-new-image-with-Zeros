import cv2
import numpy as np

goruntu = cv2.VideoCapture(0)

while True:
    ret,ressim=goruntu.read()
    
    cv2.line(ressim,(10,0),(10,200),(0,0,255),5)

    cv2.circle(ressim,(150,150),(100),(0,0,255),2)  

    cv2.putText(ressim,"ali",(150,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
    
    cv2.imshow("aa",ressim)
    
    

    if cv2.waitKey(30) & 0xFF == 32:
        break
    

ressim.release()
cv2.destroyAllWindows()
