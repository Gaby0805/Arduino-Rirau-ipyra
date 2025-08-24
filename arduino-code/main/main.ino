#include <SoftwareSerial.h>
#include <Servo.h>

SoftwareSerial esp(8, 9); // RX, TX do Arduino -> TX/RX do ESP
Servo meuServo;
Servo meuServo2;

const char* ssid = "SIM - URSO";
const char* password = "moca0621";

void sendCommand(String command, unsigned long timeout = 5000) {
  esp.println(command);
  unsigned long time = millis();
  while (millis() - time < timeout) {
    while (esp.available()) {
      char c = esp.read();
      Serial.write(c);
    }
  }
  Serial.println();
}

void setup() {
  Serial.begin(9600);
  esp.begin(9600);

  meuServo.attach(5); // pino do Arduino ligado ao servo
  meuServo.attach(6); // pino do Arduino ligado ao servo

  Serial.println("Iniciando ESP8266...");

  sendCommand("AT");
  sendCommand("AT+CWMODE=1");

  String cmd = "AT+CWJAP=\"" + String(ssid) + "\",\"" + String(password) + "\"";
  sendCommand(cmd, 10000);

  sendCommand("AT+CIFSR");
  sendCommand("AT+CIPMUX=1");
  sendCommand("AT+CIPSERVER=1,80");

  Serial.println("Servidor iniciado. Acesse pelo navegador o IP mostrado acima.");
}

void loop() {
  if (esp.available()) {
    String request = esp.readStringUntil('\n'); // lê uma linha da requisição
    Serial.println(request);

    // Checa se é uma requisição HTTP GET
    if (request.indexOf("GET /") != -1) {
      Serial.println("Requisição recebida! Ativando servo...");
      ativarServo();

      // Prepara resposta HTTP completa
      String html = "HTTP/1.1 200 OK\r\n";
      html += "Content-Type: text/html\r\n";
      html += "Connection: close\r\n\r\n"; // importante: fecha conexão
      html += "<!DOCTYPE html><html><body><h1>Servo ativado!</h1></body></html>";

      // Informa ao ESP o tamanho da resposta
      esp.print("AT+CIPSEND=0,");
      esp.println(html.length());
      delay(50); // pequeno delay para o ESP processar
      esp.print(html);
      delay(50);

      // Fecha a conexão
      sendCommand("AT+CIPCLOSE=0", 2000);
    }
  }
}


void ativarServo() {
  meuServo.write(90);
    meuServo2.write(180); // gira servo para 90°
 // gira servo para 90°
  delay(1000);        // mantém 1 segundo
  meuServo.write(0);
    meuServo2.write(0);  // retorna para posição inicial
  // retorna para posição inicial
}

