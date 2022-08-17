import numpy as np
import cv2

"""
sıfırdan resim oluşturdum zeros ile.
"""
resim=np.zeros((300,300,3),dtype="uint8")


"""
oluşturduğum resmin üzerine çizgi çektim.
"""
"""
cv2.line(hangi resim,(başlayacağı konum),(biteceği konum),(BGR renk aralığı),kalınlığı)
"""
cv2.line(resim,(0,0),(150,150),(20,60,255),5)

"""
cv2.circle(hangi goruntu,(merkezin konumu),(yarıçapı),(BGR renk aralığı),kalınlığı)
"""
cv2.circle(resim,(150,150),(20),(0,255,0),2)

""" 
cv2.putText(resim,"Deneme yazi",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(200,20,0),3)
"""
cv2.putText(resim,"Deneme yazi",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(200,20,0),3)

cv2.imshow("çizgi",resim)

cv2.putText()


cv2.waitKey(0)
cv2.destroyAllWindows()
