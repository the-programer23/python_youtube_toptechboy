#include "DHT.h"
#define DHTPIN 4
#define DHTTYPE DHT11
DHT TH(DHTPIN,DHTTYPE);

float humidity;

int setTime=500;
int dt=1000;

void setup() {
  Serial.begin(115200);
  TH.begin();
  delay(setTime);
}

void loop() {
  humidity=TH.readHumidity();
  Serial.println(humidity);
  delay(dt);
}
