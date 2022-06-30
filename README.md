# Touchless-Keyboard
I created a touchless keyboard that identifies finger strokes via computer vision and outputs sound with a buzzer controlled by an Arduino microcontroller. I used Google's `MediaPipe`, a pretrained model for hand detection. The distances between each landmark (red dots) on the hand  were initially measured by ratios which were relative to the output screen. Using `openCV` library, I found the dimensions of my webcam in pixels and multiplied the total length and witdh of my screen by these ratios in order to get proper x,y coordinates for each landmark. To activate a note certain landmark's y-coordinates must fall below the y-coordinate of another specific landmark. This information is sent to the Arduino, I used the `serial` and `vpython` libraries to help with this. Depending on what information python was sending through the serial port (notes in this case) the Arduino had corresponding frequencies the buzzer must play for each note. 



https://user-images.githubusercontent.com/106715980/176570977-15f9990f-f2eb-4e7b-b237-7e93516a3fc2.mp4









