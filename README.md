# Sightspeak
 
**SightSpeak** is an AI-powered FastAPI backend that allows visually impaired users to "see" through image understanding. By uploading images or capturing them via webcam, the system generates spoken descriptions, detects objects, and reads text from the image aloud using OCR and TTS.

## 🧠 Features
- 📸 **Image Captioning** – Generates natural-language descriptions of images
- 🧍 **Object Detection** – Detects multiple objects with YOLOv8
- 🧾 **OCR** – Extracts and reads text from signs, boards, or any image
- 🔊 **Text-to-Speech** – Converts all outputs to speech
- 🎥 **Webcam Integration** – Captures real-time frames for analysis

## 🚀 Tech Stack
- **FastAPI** (Backend API)
- **Transformers** & **YOLOv8** (AI Models via Hugging Face & Ultralytics)
- **OpenCV** (Webcam)
- **EasyOCR** (Text Detection)
- **gTTS + Playsound** (Speech Output)
