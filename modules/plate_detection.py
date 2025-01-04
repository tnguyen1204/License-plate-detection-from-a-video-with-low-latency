def detection_from_picture(frame,time_stamp_frame):
    import cv2
    from matplotlib import pyplot as plt
    import numpy as np
    import imutils
    import easyocr

    #print('Library sucessfully imported')
    
    annoted_frame = None
    
    picture_1 = frame
    picture_2 = cv2.cvtColor(picture_1,cv2.COLOR_BGR2GRAY)

    #Noise reduction
    bfilter = cv2.bilateralFilter(picture_2,11,17,17)

    #Edge detection 
    picture_3 = cv2.Canny(bfilter,30,200)

    #Contour detection 
    keypoints = cv2.findContours(picture_3,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted (contours,key = cv2.contourArea,reverse=True)[:10] #Recupère les 10 contour qui ont le plus d'air
    location = None
    for contour in contours :
        approx = cv2.approxPolyDP(contour,5,True)
        #print (len(approx))
        if len(approx) == 4 : #Detection rectangle
            location = approx
            #print('Plate number localized !')
            #Finding the plate 
            mask = np.zeros(picture_2.shape, np.uint8) #Created a black picture at the same picture_2
            picture_4 = cv2.drawContours(mask,[location],0,255,-1)
            picture_4 = cv2.bitwise_and(picture_1, picture_1,mask=mask)

            #Cropped the picture only on the plate 
            (x,y) = np.where(mask==255) #Finding all the pixel which are not black
            (x1,y1) = (np.min(x),np.min(y))
            (x2,y2) = (np.max(x),np.max(y))
            picture_5 = picture_2[x1:x2+1,y1:y2+1]

            #Read the plate 
            plate = easyocr.Reader(['en'])
            plate_analyzed = None
            plate_analyzed = plate.readtext(picture_5)
            if plate_analyzed != [] : 
                plate_number = plate_analyzed[0][-2]
                plate_accuracy = round(plate_analyzed[0][-1],2)*100
                #Print the plate number on the picture
                font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                text = cv2.putText(picture_1, text = plate_number + f' (accuracy : {plate_accuracy:.2f} %)', org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
                text = cv2.rectangle(picture_1, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
            else : 
                plate_number = 'Plate detected but cannot be read'
                plate_accuracy = 0
                #Print the plate number on the picture
                font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                text = cv2.putText(picture_1, text = plate_number + f' (accuracy : {plate_accuracy:.2f} %)', org=(10,60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
                #text = cv2.rectangle(picture_1, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)

            
            text = cv2.putText(picture_1, text= f't = {time_stamp_frame:.2f} s',org = (10,20),fontFace=font, fontScale=1,color=(255,0,0),thickness=1, lineType=cv2.LINE_AA)
            annoted_frame = picture_1
            break
        #else : 
            #print('Plate number NOT localized !')
    
    print('Detection DONE')
    return annoted_frame