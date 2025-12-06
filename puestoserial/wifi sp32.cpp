#include <WiFi.h>
#include <PubSubClient.h>

const char* wifiSSID   = "TECSJ";
const char* wifiPASS   = "TECMM2025";

const char* brokerHost = "broker.emqx.io";
const int   brokerPort = 1883;

WiFiClient espClient;
PubSubClient mqtt(espClient);

#define LED_PIN 13

char deviceID[40];


void conectarWiFi() {
    WiFi.mode(WIFI_STA);
    WiFi.begin(wifiSSID, wifiPASS);

    Serial.print("Conectando a WiFi");

    while (WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
        delay(400);
    }

    Serial.println("\n✔ WiFi conectado");
    Serial.print("IP asignada: ");
    Serial.println(WiFi.localIP());
    Serial.print("MAC: ");
    Serial.println(WiFi.macAddress());
}


void reconectarMQTT() {
    while (!mqtt.connected()) {
        Serial.print("Intento de conexión MQTT... ");

        snprintf(deviceID, sizeof(deviceID), "ESP32-%ld", random(9999));

        if (mqtt.connect(deviceID)) {
            Serial.println("OK");

            mqtt.subscribe("topicName_led");
            mqtt.publish("topicName_pub", "ESP32 listo y operativo");
        } else {
            Serial.print("Error (");
            Serial.print(mqtt.state());
            Serial.println("). Reintentando en 5s...");
            delay(5000);
        }
    }
}


void mensajeMQTT(char* topic, byte* payload, unsigned int length) {
    Serial.print("Mensaje recibido en ");
    Serial.print(topic);
    Serial.print(": ");

    String msg = "";
    for (unsigned int i = 0; i < length; i++) {
        msg += (char)payload[i];
    }
    Serial.println(msg);

    if (String(topic) == "topicName_led") {
        if (msg == "on") {
            digitalWrite(LED_PIN, HIGH);
            mqtt.publish("topicName_pub", "LED activado");
        }
        else if (msg == "off") {
            digitalWrite(LED_PIN, LOW);
            mqtt.publish("topicName_pub", "LED desactivado");
        }
    }
}


void setup() {
    Serial.begin(115200);
    delay(100);

    randomSeed(analogRead(0));

    pinMode(LED_PIN, OUTPUT);

    conectarWiFi();

    mqtt.setServer(brokerHost, brokerPort);
    mqtt.setCallback(mensajeMQTT);
}


void loop() {
    if (!mqtt.connected()) {
        reconectarMQTT();
    }

    mqtt.loop();
    delay(20);
}
