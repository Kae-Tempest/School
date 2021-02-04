#include <math.h>

#define LIGHT_SENSOR A0
const int ledPin=12;                 
const int thresholdvalue=10;
float Rsensor;
void setup() 
{
    Serial.begin(9600);
    pinMode(ledPin,OUTPUT);
}
void loop() 
{
    int sensorValue = analogRead(LIGHT_SENSOR); 
    Rsensor = (float)(1023-sensorValue)*10/sensorValue;
    Serial.println("the analog read data is ");
    Serial.println(sensorValue);
    Serial.println("the sensor resistance is ");
    Serial.println(Rsensor,DEC);
    delay(3000);

    float lux = 658.3;
    float Value_Lux = (float) (lux * sensorValue) / 1000;
    Serial.print(Value_Lux);
    Serial.print(" lux \n");


    
}
