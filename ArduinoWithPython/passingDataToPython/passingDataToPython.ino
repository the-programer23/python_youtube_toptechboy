int x=1;
int y=2;
int z=3;
int DL=1000;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  x+=2;
  y+=5;
  z+=4;
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.println(z);
  // tHE SERIAL MONITOR HAS TO BE CLOSED TO SEND DATA TO PYTHON
  delay(DL);
}
