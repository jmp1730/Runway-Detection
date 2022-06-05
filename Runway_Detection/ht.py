import cv2
import numpy as np

def h_transform(path):
    img = cv2.imread(path)
    img2 = cv2.imread('sample_out.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,120,255,apertureSize =3)
    lines = cv2.HoughLines(edges,2,np.pi/180,120)
    print(lines)
    for line in lines:
        rho = line[0][0]
        theta = line[0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img2,(x1,y1),(x2,y2),(0,0,200),1)

    cv2.imwrite('result.jpg',img2)

if __name__=='__main__':
    h_transform('NWPU-RESISC45/runway/runway_651.jpg')    