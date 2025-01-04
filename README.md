# License plate detection from a video with low latency

## Goal of the repo
The goal of the repo is to detect all the license plate from a video (.mp4). It analyzed a frame and then assess : the number on the plate, the accuracy of the detection and when in the video this car appears. 

![Plate at 5 42 s](https://github.com/user-attachments/assets/0b96dd0a-dab3-4790-b8db-b35bd1aabb96)

From all the analyzed frame, if a plate is detected then it save it in a folder. Like so with again : the number on the plate, the accuracy and the time stamp

![image](https://github.com/user-attachments/assets/b875f4f3-23ca-4abc-89d8-d52dc2b34f0d)


## How to use this repo 
1. Place your .mp4 file in the file (modify the path in main.py)
2. If you are on Windows double click on the launch.bat
3. main.py create the new folder for your annoted pictures

## How this repo detect the plate ? 
1. Open the video with open CV
2. Every 10 frames it analysed the frame as a picture by using plate_detection_from_picture.py
3. plate_detection_from_picture.py then process couples operations on the picture : grayed, noise reduction, edge detection, find the plate, read the plate and assess the accuracy. And then return an annoted picture of the frame
5. main.py then save all the plate detected on the video with the name of the plate, the accuracy and the time stamp on it 

## Limits of the repo
The goal of this repo is to be used in real time application. In order to do so, I aimed for the lowest latency therefore I used an edged based detection in order to find the plate. During my tests I noticed that sometime the plate is not detected, a good improvement would be to compare this method with a YOLO based plate detection (and then keep the same program for reading the plate). 
#### However please to that the algorithms for the edge detection and the noise reduction can be fine tunned for your application !

Here is an exemple of a YOLO based plate detection : 

![Idée d'amélioration utiliser YOLO](https://github.com/user-attachments/assets/6003d4cb-4465-4783-802c-20b8f42784b3)
