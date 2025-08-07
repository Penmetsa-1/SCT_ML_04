# SCT_ML_04

✋ Hand Gesture Recognition System

This project is a real-time hand gesture recognition system that allows you to:
- 📸 Collect your own custom gesture images using a webcam
- 🧠 Train a gesture classifier on grayscale image data
- 🎯 Predict gesture labels in real-time with high accuracy

---

📁 Dataset Creation

We created a custom dataset using OpenCV by capturing grayscale hand gesture images inside a defined region of interest (ROI) from a live webcam feed.

 🛠️ Data Collection Script Highlights:
- Capture grayscale hand images within a 300x300 ROI
- Automatically saves gesture images into subfolders (each folder = one gesture label)
- Each image is saved in `.png` format
- Labels are assigned dynamically by pressing `'n'` and typing the label name

```bash
📂 gesture_dataset/
├── HI/
│   ├── HI_0.png
│   ├── HI_1.png
│   └── ...
├── up/
│   ├── up_0.png
│   └── ...
└── small/
    ├── small_0.png
    └── ...

 🔑 Controls:
Press n → Input new gesture label (creates new subfolder)

Press s → Save current frame (grayscale cropped image)

Press q → Quit data collection
🧠 Model Training
We trained a Convolutional Neural Network (CNN) on the captured gesture dataset. Each image was:

Resized and normalized

One-hot encoded by label

Used in a stratified train-test split

🧪 Classification Report:
              precision    recall  f1-score   support

          HI       1.00      1.00      1.00         4
        down       1.00      1.00      1.00         4
         one       1.00      0.80      0.89         5
       small       0.86      1.00      0.92         6
       three       1.00      1.00      1.00         8
         two       0.86      0.86      0.86         7
          up       1.00      1.00      1.00         5

    accuracy                           0.95        39
   macro avg       0.96      0.95      0.95        39
weighted avg       0.95      0.95      0.95        39

✅ Overall Accuracy: 95%
📊 High precision and recall achieved across all gesture classes.

📌 Project Stack
Python 3

OpenCV for image capture

TensorFlow/Keras or Sklearn for training

Matplotlib and Seaborn for evaluation

🚀 Future Work
Real-time prediction using webcam feed

Expand dataset with more diverse hand shapes and lighting

Improve model with CNN + Data Augmentation

