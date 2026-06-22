from flask import Flask, request
import cv2
import numpy as np
import threading
import queue
import requests
import tensorflow as tf
import time

# ==========================================
# SURGICAL BYPASS FOR KERAS MISMATCH BUG
# ==========================================
# 1. Save the original Dense layer setup function
original_dense_init = tf.keras.layers.Dense.__init__

# 2. Create a fake setup function that deletes the bugged word
def patched_dense_init(self, *args, **kwargs):
  kwargs.pop('quantization_config', None) # Delete the word!
  original_dense_init(self, *args, **kwargs) # Run normally

# 3. Trick TensorFlow into using our fake function
tf.keras.layers.Dense.__init__ = patched_dense_init
# ==========================================

app = Flask(__name__)
frame_queue = queue.Queue(maxsize=10)

# ==========================================
# 1. Load AI & Face Detection Tools
# ==========================================
print("Loading Custom Keras Model...")
model = tf.keras.models.load_model('local_full_emotion_model.keras')


# We use OpenCV's built-in Haar Cascade to find the face box
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# The 7 emotions in alphabetical order (How Colab sorted them)
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# ==========================================
# 2. ESP32-C3 OLED Configuration
# ==========================================
ESP32_C3_IP = "http://172.21.61.20" 
last_sent_emotion = "" 

def send_emotion_to_oled(emotion):
  global last_sent_emotion
  if emotion != last_sent_emotion and emotion != "Scanning...":
    try:
      url = f"{ESP32_C3_IP}/set_emotion?val={emotion}"
      requests.get(url, timeout=1.0) 
      print(f"--> SUCCESS: Sent '{emotion}' to OLED Eyes!")
      last_sent_emotion = emotion
    except Exception as e:
      print("--> ERROR: Could not reach OLED.")

# ==========================================
# 3. Flask Web Server
# ==========================================
@app.route('/detect', methods=['POST'])
def receive_image():
  raw_data = request.data
  nparr = np.frombuffer(raw_data, np.uint8)
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

  if img is not None:
    # Fix #1: Kick out the oldest frame if the queue is full
    if not frame_queue.full():
      frame_queue.put(img)
    return "OK", 200
  else:
    return "Failed", 400

def run_flask():
  app.run(host='172.21.61.8', port=5000, use_reloader=False) #my local pc ipaddress as local

# ==========================================
# 4. Main Video & AI Loop
# ==========================================
if __name__ == '__main__':
  print("=========================================")
  print("Starting Final Year Project AI Server (Custom Model)...")
  threading.Thread(target=run_flask, daemon=True).start()
  print("=========================================")

  frame_counter = 0
  current_emotion = "Scanning..."

  while True:
    if not frame_queue.empty():
      frame = frame_queue.get()
      frame_counter += 1

      # Convert frame to Grayscale (Required for Face Detection and our Model)
      gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      # Run AI every 5 frames (Custom models are much faster than DeepFace!)
      if frame_counter % 5 == 0:

        # timer ai processing time
        start_time = time.time() 

        # 1. Find the faces in the image
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        if len(faces) > 0:
          # Just grab the first face found [x, y, width, height]
          (x, y, w, h) = faces[0]

          # 2. Crop the face out of the image
          roi_gray = gray_frame[y:y+h, x:x+w]
          
          # 3. Resize it to 48x48 pixels (What your Colab model expects)
          roi_gray = cv2.resize(roi_gray, (48, 48))
          
          # 4. Normalize the pixels (Scale from 0-255 down to 0.0-1.0)
          roi = roi_gray.astype('float') / 255.0
          
          # 5. Reshape it for Keras: (1 image, 48 pixels, 48 pixels, 1 color channel)
          roi = np.expand_dims(roi, axis=0)
          roi = np.expand_dims(roi, axis=-1)

          # 6. Predict the emotion!
          prediction = model.predict(roi, verbose=0)
          max_index = int(np.argmax(prediction))
          current_emotion = emotion_labels[max_index]

          # Draw a box around the face
          cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
          
          # Send to OLED in the background
          threading.Thread(target=send_emotion_to_oled, args=(current_emotion,)).start()
        else:
          current_emotion = "No Face Found"

          end_time = time.time() # STOP TIMER HERE

      # Draw the text on the screen
      cv2.putText(frame, f"Emotion: {current_emotion}", (20, 40), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

      cv2.imshow("ESP32-S3 Live Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
      
  cv2.destroyAllWindows()

