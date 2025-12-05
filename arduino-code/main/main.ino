  #include <ESP8266WiFi.h>
  #include <WebSocketsClient.h>
  #include <Servo.h>
  const char* ssid = "IOT";
  const char* password = "IoTf2025f1";

  const char* websocket_server_host = "arduino-rirau-ipyra.onrender.com";
  const uint16_t websocket_server_port = 443; 
  const char* websocket_path = "/socket/";

  const int servoPin = D1;
  const int servoPin2 = D3;

  Servo meuServo;
  Servo meuServo2;

  const unsigned long tempoSegurar = 2000;

  WebSocketsClient webSocket;

  void moverServos() {
    Serial.println("Servos ativados");
    meuServo.write(180);
    meuServo2.write(180); 
    delay(tempoSegurar); 
    meuServo.write(0);
    meuServo2.write(0);
    Serial.println("Servos retornaram à posição inicial");




    

  }

  void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
    switch (type) {
      case WStype_DISCONNECTED:
        Serial.println("WebSocket desconectado");
        break;
      case WStype_CONNECTED:
        Serial.println("WebSocket conectado!");
        webSocket.sendTXT("ESP8266 conectado");
        break;
      case WStype_TEXT:
        Serial.printf("Mensagem recebida: %s\n", payload);

        
        if (String((char*)payload) == "ALARME") {
          moverServos();
        } 
        break;
      default:
        break;
    }
  }

  void setup() {
    Serial.begin(9600);

    
    WiFi.begin(ssid, password);
    Serial.println("Conectando ao WiFi...");
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("\nWiFi conectado!");
    Serial.println(WiFi.localIP());

    
    meuServo.attach(servoPin);
    meuServo.write(0);
    meuServo2.attach(servoPin2);
    meuServo2.write(0);

    
    webSocket.beginSSL(websocket_server_host, websocket_server_port, websocket_path);
    webSocket.onEvent(webSocketEvent);
    webSocket.setReconnectInterval(5000); 
  }

  void loop() {
    webSocket.loop();
  }
