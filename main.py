import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import os
from termcolor import colored
from modules.plate_detection import detection_from_picture

file = "C:/Users/TheoN/Desktop/Car plate from video/Sample_plate.mp4"


#Opening the file
cap = cv2.VideoCapture(file)
print(f"File path : {file}")
print(f"Video status : {cap.isOpened()}")
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS of the video is : {fps}")

#Checking if the file is playable
if not cap.isOpened(): 
    print('Error, cannot open the file')
    exit()

#Let's read the film
i = 0
while True:
    ret, frame = cap.read()     
    if not ret: 
        print("The video is ended")
        break

    if i%10 == 0 : #Analyse de l'image toutes les 10 frames 
        time_stamp = i / fps
        print(colored((f'Frame at {time_stamp:0.2f} s'),"red"))
        annoted_frame = detection_from_picture(frame,time_stamp)
        if annoted_frame is not None : 
            print('Plate found !')
            cv2.imshow('Video', annoted_frame)
            # Save the results in a folder
            output_folder = "Pictures of the plates"
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            output_path = os.path.join(output_folder, f"Plate at {time_stamp:0.2f} s.jpg")
            cv2.imwrite(output_path, annoted_frame)
            print(f"Annoted frame saved at : {output_path}")
            if cv2.waitKey(25) & 0xFF == ord('q'):
                print("The video has been interrupted by the user")
                break
        else : 
            print('Plate number NOT found')
    i+=1
    
cap.release()
cv2.destroyAllWindows()


#TEST FONCTIONNEMENT SUR UNE IMAGE

# frame = cv2.imread('image1.jpg')
# frame_annoted = detection_from_picture(frame,2)
# #Enregistrement de l'image dans un autre dossier
# output_folder = "Pictures of the plates"
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
# output_path = os.path.join(output_folder, "annoted_frame.jpg")
# cv2.imwrite(output_path, frame_annoted)
# print(f"Image annotée sauvegardée sous : {output_path}")
# cv2.imshow('Automatic plate detection', frame_annoted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
