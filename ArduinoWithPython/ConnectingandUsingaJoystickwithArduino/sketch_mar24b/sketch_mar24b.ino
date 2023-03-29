int potX=A0;
int potY=A1;
int potZ=12;

int xVal=0;
int yVal=0;
int zVal=0;

int dt=100;
void setup() {
 Serial.begin(115200);
 pinMode(potX,INPUT);
 pinMode(potY,INPUT);
 pinMode(potZ,INPUT); 
 digitalWrite(potZ,LOW);
}

void loop() {
  xVal=analogRead(potX);
  yVal=analogRead(potY);
  potZ=digitalRead(potZ);
  Serial.print(xVal);
  Serial.print(",");
  Serial.print(yVal);
  Serial.print(",");
  Serial.println(potZ);
  delay(dt);
}
