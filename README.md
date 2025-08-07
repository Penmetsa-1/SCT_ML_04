# SCT_ML_04
 ✋ Hand Gesture Recognition using CNN

This project is a **real-time hand gesture recognition system** that allows users to train custom gestures using a webcam and classify them using a **Convolutional Neural Network (CNN)**. The model is trained on grayscale images of hand gestures collected and labeled manually.

---

📌 Features

- 📸 Live hand gesture capture using webcam
- 🗂️ Automatic dataset creation with custom labels
- 🎯 Image pre-processing and augmentation
- 🧠 CNN model training and evaluation
- 📊 Confusion matrix and classification report
- ✅ Real-time or test-set prediction

---

 📂 Project Structure

 
---

## 🚀 How It Works

### 1. Data Collection
- Run a Python script to capture hand gestures using a webcam.
- Press `n` to create a new gesture class (e.g., "thumbs_up").
- Press `s` to save grayscale hand ROI images.
- Saved images are stored in `gesture_dataset/<gesture_name>/`.

### 2. Model Training (Google Colab)
- Dataset is loaded, resized, and normalized.
- A CNN model is built using TensorFlow/Keras.
- Training, validation, classification report, and confusion matrix are generated.
- Final model is saved as `gesture_model.h5`.

### 3. Real-Time Prediction (Optional)
- Use the saved model to detect gestures from webcam input in real-time.

---

## 📊 Model Summary

- **Architecture**: CNN with Conv2D, MaxPooling2D, Dense, and Dropout layers
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: Adam
- **Accuracy Achieved**: _~90–98% (depends on data quality and number of classes)_

---

## 🛠️ Tech Stack

- Python
- OpenCV
- TensorFlow / Keras
- NumPy, Matplotlib, Seaborn
- Google Colab (for training)

---

## 📈 Evaluation Metrics

- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)
- Test Prediction Visualization

---

## 📥 Installation

```bash
pip install opencv-python
pip install tensorflow
pip install matplotlib seaborn

✅ Usage
🎓 Training in Colab
Upload gesture_dataset folder

Run the training notebook cell-by-cell

Download the gesture_model.h5 for real-time usage

🖥️ Real-Time Prediction (Local)
Load the model

Capture live webcam feed

Predict gestures in real-time

| Input Gesture | Predicted |
| ------------- | --------- |
| ✊ Fist        | Fist      |
| 👍 Thumbs Up  | Thumbs Up |
| ✋ Palm Open   | Stop      |


