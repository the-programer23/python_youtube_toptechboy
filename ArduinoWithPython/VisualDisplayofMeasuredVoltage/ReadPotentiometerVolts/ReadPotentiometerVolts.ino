int myVoltPin = A2;
int readVal;
float V2;
int waitT = 250;
int ledPin = 9;
 
void setup() {
  Serial.begin(9600);
  pinMode(ledPin , OUTPUT);
  pinMode(myVoltPin, INPUT);
}

void loop() {
 readVal = analogRead(myVoltPin);
 V2 = (5. / 1023.) * readVal;
 //Serial.print("Potentiometer voltage is: ");
 Serial.println(readVal);
 
 if(V2 > 4.0){
  //Serial.println("V2 > 4.0");
  digitalWrite(ledPin, HIGH);
 }else {
  digitalWrite(ledPin, LOW);
 }
 
 delay(waitT);  
}
