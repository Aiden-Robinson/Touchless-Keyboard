import cv2
import serial
from vpython import *

import mediapipe as mp
import time

arduinoData= serial.Serial('com7', 9600) #specifying the serial port and baud rate
cap= cv2.VideoCapture(0) #initializing the use of the webcam as the video capturing device
mpHands= mp.solutions.hands #variable to
hands= mpHands.Hands() #initializing the hand class from Mediapipe, leaving parameters becasue the default is acceptable
mpDraw= mp.solutions.drawing_utils #importing the tools to draw on the landmark detections

pTime=0 #previous time
cTime= 0 #current time



while True:
    ret, img= cap.read() #storing the video from the webcame to a variable called img
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #OpenCV by default runs on BGR, but we need to convert to RBG for Mediapipe
    results= hands.process(imgRGB) #running the hand detection on the RBG version of the webcam input

    if results.multi_hand_landmarks: #if it detects a landmark (if a quantity of landmarks exists, this is true or false)
        for handLandmarks in results.multi_hand_landmarks: #seperating all of the detected landmarks into individual landmarks
            landmarkList=[] #creates an ampty list to store the coordinated of all landmarks
            for id, lm in enumerate(handLandmarks.landmark): #enumerating landmark information to seperate into ID and position (x and y)
                height, width, chanel= img.shape #obtaining height and width of our
                cx,cy= int(lm.x*width), int(lm.y*height) #the current coordinated of the landmarks are relative to the size of the output screen so we need to convert the ratios into actual x, y coordinates on the output scrren
                landmarkList.append([id,cx,cy]) #appends the id and x y coordinates of each landmark to a list of landmarks

        if landmarkList:
            if landmarkList[8][2]>landmarkList[6][2]: #when the y-coordinate of a speific landmark passes the y-coordinate of another specific landmark
                cv2.circle(img,(landmarkList[8][1],landmarkList[8][2]),25,(255,0,0),cv2.FILLED) #on one of the specific landmarks, draw a blue circle
                command= "noteD" #the command that will be sent to the arduino
                command = command + '\r' #adding a CRLF (carriage return and line feed) so the arduino knows when to stop reading from the serial
                arduinoData.write(command.encode()) #sending over the data
            elif landmarkList[12][2]>landmarkList[10][2]:
                cv2.circle(img,(landmarkList[12][1],landmarkList[12][2]),25,(255,0,0),cv2.FILLED)
                command= "noteE"
                command = command + '\r'
                arduinoData.write(command.encode())
            elif landmarkList[16][2]>landmarkList[14][2]:
                cv2.circle(img,(landmarkList[16][1],landmarkList[16][2]),25,(255,0,0),cv2.FILLED)
                command= "noteF"
                command = command + '\r'
                arduinoData.write(command.encode())
            elif landmarkList[20][2]>landmarkList[18][2]:
                cv2.circle(img,(landmarkList[20][1],landmarkList[20][2]),25,(255,0,0),cv2.FILLED)
                command= "noteG"
                command = command + '\r'
                arduinoData.write(command.encode())
            elif landmarkList[4][2]>landmarkList[5][2]:
                cv2.circle(img,(landmarkList[4][1],landmarkList[4][2]),25,(255,0,0),cv2.FILLED)
                command= "noteC"
                command = command + '\r'
                arduinoData.write(command.encode())
            else:
                command= "OFF" #if there are no landmarks detected, the command sent to the arduino will be to turn the buzzer off
                command = command + '\r'
                arduinoData.write(command.encode())

        mpDraw.draw_landmarks(img,handLandmarks, mpHands.HAND_CONNECTIONS)#drawing red lines between all landmarks for visual enhancement




    cv2.imshow("Image", img) #continually outputting the screen with all additions made to the intial webcam capture screen
    if cv2.waitKey(1)==ord('q'): #if the user presses q then the program stops
        break

