#include <DHT.h>
#define DHTPIN 0 
#define DHTTYPE DHT22 
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(9600);
  }

void loop() {
  delay(2000);
  float T = dht.readTemperature();
  float H = dht.readHumidity();

  if (isnan(T)){
    Serial.println(" Erreur de lecture du capteur DHT!");
    return;
  }
Serial.println(T);
Serial.println(H); 
  }
