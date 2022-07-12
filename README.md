# Touchless-Keyboard
I created a touchless keyboard that identifies finger strokes via computer vision and outputs sound with a buzzer controlled by an Arduino microcontroller. I used Google's `MediaPipe`, a pretrained model for hand detection. The distances between each landmark (red dots) on the hand  were initially measured by ratios which were relative to the output screen. Using `OpenCV` library, I found the dimensions of my webcam in pixels and multiplied the total length and witdh of my screen by these ratios in order to get proper x,y coordinates for each landmark. To activate a note certain landmark's y-coordinates must fall below the y-coordinate of another specific landmark. This information is sent to the Arduino, I used the `serial` library to help with this. Depending on what information python was sending through the serial port (notes in this case) the Arduino had corresponding frequencies the buzzer must play for each note. 

`Skills used`: Python, C++, OpenCV, Mediapipe, Circuiting, Python-Arduino communication

## (Watch with sound)
https://user-images.githubusercontent.com/106715980/176570977-15f9990f-f2eb-4e7b-b237-7e93516a3fc2.mp4

# Python Libaries Used
- `Google's Mediapipe` was used to 
- `OpenCV`
- `Serial`


# Simple Arduino buzzer circuit 

<img width= "500" height = "550" src= "https://user-images.githubusercontent.com/106715980/176573268-09a15263-f2df-4569-bb26-8e0b2712be11.JPG">

# What I learned
The most difficult part of the project for me was figuring out how to have the Arduino communicate with the python code through the serial port. I learned that the port cannot send and recieve data at the same time. After learning the approproate python libraries, and which side of the port should be opened at a given time, I got them communicating. This opens up a whole world of projects I can do with the arduino and python code in thr future.

# Steps Moving Forward
At the time of creation I was limited to one active buzzer. If I were able to aquire another one, I would love to explore the use of chords (multiple fingers activating a key at once). Although I used a pretrained hand model from google, it got me super curious and creating my own machine learning model, so that is what I will work on in my next project!


