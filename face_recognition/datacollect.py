import cv2
import face_recognition


known_face_encodings=[]  # bos listeler tanımlandı
known_face_names=[]     #bos liste tanımlama 2

#Tanınan Kişilerin Görüntülerinin Yüklenmesi 
known_person1_image=face_recognition.load_image_file("person1.jpg")
known_person2_image=face_recognition.load_image_file("person2.jpg")



#Tanınan Kişilerin Görüntülerinin kodlanması
known_person1_image=face_recognition.face_encodings(known_person1_image)[0]
known_person2_image=face_recognition.face_encodings(known_person2_image)[0]


#Tanınan Yüz Kodlamalarının Listeye Eklenmesi:


known_face_encodings.append(known_person1_image)
known_face_encodings.append(known_person2_image)


#Tanınan Yüz İsimlerinin Listeye Eklenmesi:Q


known_face_names.append("jeff")
known_face_names.append("messi")



#Video Akışının Başlatılması ve İşlenmesi:


video_capture=cv2.VideoCapture(0)

while True:
    ret,frame=video_capture.read()
    face_locations=face_recognition.face_locations(frame) #yüz konumlarını bulur
    face_encodings=face_recognition.face_encodings(frame,face_locations) # yüz kodlarını alır
    for (top,right,bottom,left), face_encoding in zip(face_locations, face_encodings): # yüzleri tanır
        matches=face_recognition.compare_faces(known_face_encodings, face_encoding)    #yüzleri tanırın devamı

        Name="Bilinmeyen"
        if True in matches: # eşleşen isimleri bulur 
            first_mathc_index=matches.index(True) # eşleşen isimleri bulur devamı
            Name=known_face_names[first_mathc_index] # eşleşen isimleri bulur  devamı
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,250),2) # cerceveye isimve yüz ekleme 
        cv2.putText(frame,Name,(left,top-10),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(0,0,255),2) # cerceveye isimve yüz ekleme 2
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break   
video_capture.release()
cv2.destroyAllWindows()