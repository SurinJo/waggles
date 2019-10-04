#include <dht.h>
#define DHT11_PIN 7

//----voltage sensor setting
int analogInput = A1;
float vout = 0.0;
float vin = 0.0;
float R1 = 30000.0; 
float R2 = 7500.0; 
int value = 0;

//----dht11 sensor setting
dht DHT;

void setup(){
  pinMode(analogInput, INPUT);
  Serial.begin(9600);
  Serial.println("Temperature,Humidity,Voltage");
}

void loop()
{
  //----voltage sensor
  value = analogRead(analogInput);
  vout = (value * 5.0) / 1024.0; // see text
  vin = vout / (R2/(R1+R2)); 
  
  //----dht11 sensor
  int chk = DHT.read11(DHT11_PIN);
  Serial.print(DHT.temperature);
  Serial.print(",");
  Serial.print(DHT.humidity);
  Serial.print(",");
  Serial.print(vin-1.4,2);
  Serial.println();
  
  delay(500);
}
