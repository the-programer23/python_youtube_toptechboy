String myCmd;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(13,OUTPUT);
}

void loop() {
  while(Serial.available()==0){
    
  }
  myCmd=Serial.readStringUntil('\r');
  if(myCmd=="ON"){
    digitalWrite(13,HIGH);
  }
  if(myCmd=="OFF"){
    digitalWrite(13,LOW);  
  }
}
