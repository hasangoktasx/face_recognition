import cv2
import face_recognition
img=cv2.imread("images/jeff.jpg") #resmi okuttuk
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #renk dönüştürdük
img_encoding=face_recognition.face_encodings(rgb_img)[0]#yüzü kodladık

img2=cv2.imread("images/images.jpg")
rgb_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img_encoding2=face_recognition.face_encodings(rgb_img2)[0]

result=face_recognition.compare_faces([img_encoding], img_encoding2) #yüzü karsılastırdık
print("Result:",result) 

cv2.imshow("Img",img)
cv2.imshow("Img2",img2)
cv2.waitKey(0)
