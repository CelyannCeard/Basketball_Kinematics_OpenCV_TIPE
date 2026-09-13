# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:42:39 2024

@author: celya
"""

import cv2
import numpy as np

# Charger la vidéo
cap = cv2.VideoCapture('Cuir_Beton.mp4')

# Définir les bornes de couleur
l = np.array([0, 100, 0])
u = np.array([180, 255, 255])
kernel = np.ones((5, 5), np.uint8)

# Obtenir la hauteur et la largeur d'une frame
width = int(cap.get(3))
height = int(cap.get(4))

# Réduire la taille de la vidéo à 40%
new_width = int(width * 0.4)
new_height = int(height * 0.4)

#Initialiser le compteur d'image
Nbr_Image = 0   #initialisation à 0 car la première image compte
FRAMERATE = 960

#Recherche des pixels image par image
while cap.isOpened():

    ret, frame = cap.read()

    if ret:

        # Redimensionner la frame
        frame = cv2.resize(frame, (new_width, new_height))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, l, u)

        M = cv2.moments(mask, True)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cX, cY), 10, (0, 0, 255), -1)

        mask = cv2.erode(mask, kernel)
        mask = cv2.dilate(mask, kernel)
        
        print(Nbr_Image/FRAMERATE,cY,sep=';')   #afficher le temps et la hauteur
        
        #Compter le nombre d'image
        Nbr_Image += 1
        
        #mask pour voir les pixels que le programme voit, frame pour la vidéo
        cv2.imshow("Test", mask)  
        
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
    


cap.release()
cv2.destroyAllWindows()

#Afficher le nombre d'image compté
print("Nombre d'image", Nbr_Image)