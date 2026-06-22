# 🧠 Local Facial Emotion Recognition — AI Trainer

A CNN-based facial emotion recognition model trained locally using TensorFlow/Keras. Built as a **Final Year Project** for educational purposes. The example dataset are given and if want to train with your own can follow the step below:

---

## 📋 Overview

This project trains a Convolutional Neural Network (CNN) to classify **7 facial emotions** from grayscale 48×48 images:

| Label | Emotion |
|-------|---------|
| 0 | Angry |
| 1 | Disgust |
| 2 | Fear |
| 3 | Happy |
| 4 | Sad |
| 5 | Surprise |
| 6 | Neutral |

The model architecture uses 3 convolutional blocks with BatchNormalization and Dropout for regularization, followed by a fully connected layer and a 7-class softmax output.

---

## 🗂️ Project Structure

```
python_ai_trainer/
├── dataset/
│   ├── angry/
│   ├── disgust/
│   ├── fear/
│   ├── happy/
│   ├── sad/
│   ├── surprise/
│   └── neutral/
├── train.py
└── local_emotion_model_2.keras
```

---

## 📦 Dataset Setup

This project supports combining images from **multiple dataset sources** for better generalization. You can download and merge any of the following:

### Recommended Datasets

| Dataset | Description | Link |
|---------|-------------|------|
| **CK+** (Extended Cohn-Kanade) | Lab-controlled posed expressions, high quality | [Kaggle](https://www.kaggle.com/datasets/shawon10/ckplus) |
| **FER2013** | 35,000+ grayscale 48×48 images, wild conditions | [Kaggle](https://www.kaggle.com/datasets/msambare/fer2013) |
| **AffectNet** | Large-scale in-the-wild facial expressions | [Official Site](http://mohammadmahoor.com/affectnet/) |
| **RAF-DB** | Real-world Affective Faces Database | [Official Site](http://www.whdeng.cn/RAF/model1.html) |

### How to Combine Datasets

1. Download your chosen datasets
2. Sort images into the 7 emotion folders under `dataset/`
3. Make sure each subfolder name **exactly matches** the emotion label
4. Images of **any size or resolution** are accepted — the trainer automatically resizes all images to 48×48 grayscale

> **Tip:** The more diverse your data sources, the better your model generalizes to real-world faces.

---

## ⚙️ Requirements

```bash
pip install tensorflow
```

Tested with:
- Python 3.8+
- TensorFlow 2.x

---

## 🚀 How to Run

1. Place your dataset in the correct folder structure (see above)
2. Update `dataset_path` and `save_path` in `train.py` to match your local paths
3. Run the trainer:

```bash
python train.py
```

The script will:
- Scan and load all images from the dataset folder
- Split 80% for training and 20% for validation automatically
- Train for up to 100 epochs with early stopping (stops if validation loss stops improving for 5 consecutive epochs)
- Save the best model to `local_full_emotion_model.keras`

---

## 📊 Output

After training completes, the console will print:

```
=========================================
✅ Success! Local model saved to: <your_path>\local_full_emotion_model.keras
IMPORTANT: Class Label Mapping:
{'angry': 0, 'disgust': 1, 'fear': 2, 'happy': 3, 'neutral': 4, 'sad': 5, 'surprise': 6}
=========================================
```

> ⚠️ The class index mapping may vary depending on your folder names. Always refer to the printed `class_indices` output when using the model for inference.

---

## ⚠️ Disclaimer

**This project is for educational and academic purposes only — Final Year Project use.**

- The datasets referenced (CK+, FER2013, AffectNet, RAF-DB) are subject to their own individual licenses and terms of use
- Users are responsible for complying with the terms of each dataset they download and use
- This repository does **not** distribute or host any dataset images
- Do **not** use this model or any combined dataset for commercial purposes without obtaining the appropriate dataset licenses

---

## 📝 License

This code is released for academic/educational use only. See individual dataset websites for their respective data licenses.

