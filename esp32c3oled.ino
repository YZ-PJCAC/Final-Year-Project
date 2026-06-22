#include <WiFi.h>
#include <WebServer.h>
#include "Face.h"

// ===========================
// 1. Enter your Network Details
// ===========================
const char* ssid = "Skip";
const char* password = "4geyi4444";

// Create the Web Server on port 80
WebServer server(80);

// Create the Face object pointer
Face *face;

// ===========================
// 2. The Emotion Brain (Handles incoming commands)
// ===========================
void handleEmotion() {
  // Check if the PC sent the "?val=" argument
  if (server.hasArg("val")) {
    String newEmotion = server.arg("val");
    Serial.println("Command Received: " + newEmotion);

    // Match the DeepFace string to the OLED Animation
    if (newEmotion == "angry") {
      face->Expression.GoTo_Angry();
      face->Look.LookAt(-0.3, 0.0);
    } 
    else if (newEmotion == "happy") {
      face->Expression.GoTo_Happy();
      face->Look.LookAt(0.3, 0.0);
    } 
    else if (newEmotion == "sad") {
      face->Expression.GoTo_Sad();
      face->Look.LookAt(0.0, 0.3);
    } 
    else if (newEmotion == "surprise") {
      face->Expression.GoTo_Surprised();
      face->Look.LookAt(0.0, -0.3);
    } 
    else if (newEmotion == "fear") {
      face->Expression.GoTo_Scared();
      face->Look.LookAt(0.0, -0.2);
    } 
    else if (newEmotion == "disgust") {
      face->Expression.GoTo_Annoyed();
      face->Look.LookAt(-0.4, 0.0);
    } 
    else {
      // If it receives "neutral" or "No Face Found"
      face->Expression.GoTo_Normal();
      face->Look.LookAt(0.0, 0.0);
    }
    
    // Reply to the PC to confirm receipt
    server.send(200, "text/plain", "OLED updated to: " + newEmotion);
  } else {
    server.send(400, "text/plain", "Error: Missing emotion value");
  }
}

// ===========================
// 3. Setup Loop
// ===========================
void setup() {
  Serial.begin(115200);
  
  // 1. Initialize the Face
  face = new Face(128, 64, 40);
  face->RandomBlink = true;
  face->RandomLook = false;    // Keep false so they look where the emotion dictates
  face->RandomBehavior = false;
  face->Blink.Timer.SetIntervalMillis(3500); // Blink every 3.5 seconds
  
  face->Expression.GoTo_Normal(); // Start with neutral eyes

  // 2. Connect to WiFi
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    face->Update(); // Keep the eyes drawing on the screen while connecting
  }
  
  // 3. Print the assigned IP Address (YOU WILL NEED THIS FOR YOUR PYTHON SCRIPT!)
  Serial.println("\n--- CONNECTED! ---");
  Serial.print("ESP32-C3 IP Address: ");
  Serial.println(WiFi.localIP());

  // 4. Start the Web Server
  server.on("/set_emotion", handleEmotion);
  server.begin();
}

// ===========================
// 4. Main Loop
// ===========================
void loop() {
  // Listen for incoming PC messages
  server.handleClient();
  
  // Keep the eye animations running smoothly
  face->Update();
}