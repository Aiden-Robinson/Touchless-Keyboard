String myCommand;
int noteC = 261; //initializing what frequences correspond to which notes
int noteD = 294;
int noteE = 330;
int noteF = 349;
int noteG = 392;
int LED=13; 
int buzzer=10; //initializing what pin the buzzer is connected to 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // initializing baud rate which is the same as in the python code
 
  pinMode(LED, OUTPUT); 
  pinMode(buzzer, OUTPUT); //setting the pin mode for the buzzer

}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() == 0) { //run a blank loop infinitely if there is nothing detected from the serial monitor

  }
  myCommand = Serial.readStringUntil('\r'); //read from the serial monitor until the CRLF specified in the python code is reached

  if (myCommand == "OFF") { //if the command was to turn off
    digitalWrite(LED, HIGH);
    noTone(buzzer); // do not activate the buzzer
  }
  if (myCommand == "noteC") { //if the command was to activate the note C
    digitalWrite(LED, HIGH); //the LED is simply for visual confirmation that the arduino is receiving the commands
    tone(buzzer, noteC);// play C on the buzzer

  }
  if (myCommand == "noteD") { //etc..
    digitalWrite(LED, HIGH);
    tone(buzzer, noteD);

  }
  if (myCommand == "noteE") {
    digitalWrite(LED, HIGH);
    tone(buzzer, noteE);

  }
  if (myCommand == "noteF") {
    digitalWrite(LED, HIGH);
    tone(buzzer, noteF);

  }
  if (myCommand == "noteG") {
    digitalWrite(LED, HIGH);
    tone(buzzer, noteG);

  }





}
