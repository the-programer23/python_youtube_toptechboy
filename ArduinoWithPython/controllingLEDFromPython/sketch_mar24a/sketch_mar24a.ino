int redPin=11;
int greenPin=10;
int bluePin=9;
int redVal=255;
int greenVal=255;
int blueVal=255;
String cmd;
void setup() {
  Serial.begin(115200);
  pinMode(redPin,OUTPUT);
  pinMode(greenPin,OUTPUT);
  pinMode(bluePin,OUTPUT);
}

void loop() {
  //while there is no data do nothing
  while(Serial.available()==0){}
  redVal=Serial.readStringUntil(':').toInt();
  greenVal=Serial.readStringUntil(':').toInt();
  blueVal=Serial.readStringUntil("\r").toInt();
  analogWrite(redPin,redVal);
  analogWrite(greenPin,greenVal);
  analogWrite(bluePin,blueVal);
  
  if(cmd=="off"){
    analogWrite(redPin,0);
    analogWrite(greenPin,0);
    analogWrite(bluePin,0);
  }

}
