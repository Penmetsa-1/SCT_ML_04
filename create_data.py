import cv2
import os

# Base directory to save gestures
DATASET_PATH = "gesture_dataset"
os.makedirs(DATASET_PATH, exist_ok=True)

# Initialize camera
cap = cv2.VideoCapture(0)

current_label = None
image_count = 0
MAX_IMAGES = 100  # Limit per gesture

print("🔄 Press 'n' to enter new gesture label.")
print("💾 Press 's' to save frame.")
print("❌ Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not accessible.")
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Define region of interest (ROI)
    x, y, w, h = 100, 100, 300, 300
    cv2.rectangle(gray, (x, y), (x + w, y + h), 255, 2)
    roi = gray[y:y+h, x:x+w]

    # Show camera frame
    cv2.imshow("Gesture Capture", gray)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('n'):
        current_label = input("✏️ Enter new gesture label: ").strip()
        gesture_folder = os.path.join(DATASET_PATH, current_label)
        os.makedirs(gesture_folder, exist_ok=True)
        image_count = 0
        print(f"🆕 New gesture started: {current_label}")

    elif key == ord('s') and current_label:
        filename = os.path.join(gesture_folder, f"{current_label}_{image_count}.png")
        cv2.imwrite(filename, roi)
        print(f"✅ Saved: {filename}")
        image_count += 1
        if image_count >= MAX_IMAGES:
            print(f"⚠️ Reached {MAX_IMAGES} images for '{current_label}'. Press 'n' for next gesture.")

    elif key == ord('q'):
        print("🛑 Quitting capture.")
        break

cap.release()
cv2.destroyAllWindows()
