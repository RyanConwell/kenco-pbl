#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid   = "STEM80211";
const char* pass   = "STEMstem";

const String target = "10.149.185.173:5000/api/restock";
const String body   = "device_id=1";


void setup() {
  // Set up serial for debugging
  Serial.begin(9600);
  delay(10);
  Serial.println();
  Serial.println();

  // Connect to WiFi network
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi Connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Connect to server
  HTTPClient http;

  Serial.println("[HTTP] begin...");
  http.begin("http://10.149.185.173:5000/api/restock");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  Serial.println("[HTTP] POST...");
  int httpCode = http.POST("device_id=1");

  String payload = http.getString();
  Serial.println(httpCode);
  Serial.println(payload);

  //
  http.end();
  ESP.deepSleep(0);
  
}

void loop() {}
