import requests
import cv2

url = "http://127.0.0.1:8000/api/process-webcam"

# open webcam
cap = cv2.VideoCapture(0)

print("📸 Press 'c' to capture frame, 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)

    if key == ord('c'):
        # Save captured frame to a temporary image file
        temp_filename = "temp_capture.jpg"
        cv2.imwrite(temp_filename, frame)

        # Send to backend
        with open(temp_filename, "rb") as f:
            files = {"file": ("filename.jpg", f, "image/jpeg")}
            try:
                print("📤 Capturing frame and sending to backend...")
                response = requests.post(url, files=files)
                print("✅ Response:", response.text)
            except Exception as e:
                print("❌ Error sending frame:", e)

    elif key == ord('q'):
        print("👋 Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
