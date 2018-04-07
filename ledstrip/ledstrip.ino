#define REDPIN 3
#define GREENPIN 5 
#define BLUEPIN 6

//stores 3 bytes of information from Serial.read()
int incoming[3];

void setup() {
  // put your setup code here, to run once:
  pinMode(BLUEPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(REDPIN, OUTPUT);
  Serial.begin(9600);
}

void setOutput(int pinNum, int intensity){
  analogWrite(pinNum, intensity);
}

void loop() {
  //Need 3 bytes of information 
  // -> {R, G, B}
  while(Serial.available() >= 3){
    for(int i = 0; i < 3; i++){
      incoming[i] = Serial.read();
    }
  }
  setOutput(REDPIN, incoming[0]);
  setOutput(GREENPIN, incoming[1]);
  setOutput(BLUEPIN, incoming[2]);
  delay(100);
}
