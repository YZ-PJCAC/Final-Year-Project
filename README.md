# Final-Year-Project
AI-Powered Eye Emotion Projection for STEM education

## Introduction
This project is a Final Year Project (FYP) that combines **Artificial Intelligence** and **Internet of Things (AIoT)** to build a real-time facial emotion recognition system. An ESP32-S3 camera module captures the user's face and sends it over Wi-Fi to a local laptop, which uses a trained deep learning model to detect the emotion. The result is then displayed on an ESP32-C3 microcontroller with an OLED screen showing animated eye expressions that match the detected emotion — all running locally with no internet connection required.


## 📦 Datasets

The model was trained on a merged combination of four publicly available facial expression datasets. All four share the same 7-emotion label structure, making them suitable for merging into a single unified training set.

| Dataset | Description | Link |
|---------|-------------|------|
| **AffectNet** | Large-scale dataset with both naturally occurring and posed facial expressions, annotated with 8 emotion categories. One of the largest FER datasets available. | [Kaggle - affectnet](https://www.kaggle.com/datasets/mstjebashazida/affectnet) |
| **CK+ (Extended Cohn-Kanade)** | A benchmark dataset of posed facial expression sequences captured in lab conditions, covering 7 emotion categories. | [Kaggle — CK+](https://www.kaggle.com/datasets/shawon10/ckplus) |
| **FER2013** | ~35,000 grayscale 48×48 facial expression images across 7 emotions. Originally from the 2013 Kaggle Facial Expression Recognition Challenge. | [Kaggle — FER2013](https://www.kaggle.com/datasets/msambare/fer2013) |
| **FER+ (FER25)** | An improved re-labelling of FER2013 by Microsoft Research, where each image was re-annotated by 10 crowd-sourced taggers for higher label accuracy. | [GitHub — FERPlus](https://github.com/microsoft/FERPlus) |

---


## 📚 References & Acknowledgements

- **ESP32-S3 CAM setup & firmware base** — [ittipu / IoT_Bhai_Youtube_Channel](https://github.com/ittipu/IoT_Bhai_Youtube_Channel/tree/b330d3f58b183840a606ab8beb32733b73c1977d/Complete%20ESP32%E2%80%91CAM%20Tutorial%20Playlist/1.%20Getting%20Started%20with%20Freenova%20ESP32-S3%20Cam%20Setup%20%26%20Web%20Server/freenova_esp32s3_cam_setup_and_webserver)
- **OLED animated eye library** — [playfultechnology / esp32-eyes](https://github.com/playfultechnology/esp32-eyes)
- **Face detection** — OpenCV Haar Cascade (`haarcascade_frontalface_default.xml`)

---

## ⚠️ Disclaimer

This project was developed purely for **academic and educational purposes** as a Final Year Project (FYP).

- All datasets used for training (AffectNet, CK+, FER2013, FER+) are publicly available research datasets intended for non-commercial use. Please refer to each dataset's individual license and terms of use before using them.
- The open-source libraries and repositories referenced in this project ([esp32-eyes](https://github.com/playfultechnology/esp32-eyes), [IoT_Bhai_Youtube_Channel](https://github.com/ittipu/IoT_Bhai_Youtube_Channel)) are credited to their respective authors. Their code was adapted and modified to suit this project's specific hardware and requirements.
- This system processes all facial image data **locally** on the user's own machine. No images or personal data are transmitted to any external server or third party.
- The emotion predictions produced by this system are based on a machine learning model and **should not be used for any real-world decision-making**, clinical diagnosis, or sensitive applications. The model may produce incorrect predictions, particularly under poor lighting conditions or with faces outside its training distribution.
- The authors of this project make no warranties regarding the accuracy or reliability of the emotion recognition output.

---

## 📄 License

This project is intended for academic use only. All third-party libraries and datasets are subject to their own respective licenses.
