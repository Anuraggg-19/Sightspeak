from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from services.captioning_service import generate_caption
from services.speech_service import text_to_speech
from services.object_detection_service import detect_object
from services.ocr_service import extract_text_from_image

from PIL import Image
import os
import uuid
import shutil

router = APIRouter()

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/process-webcam")
async def process_webcam(file: UploadFile = File(...)):
    try:
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="File is not an image.")

        file_ext = file.filename.split(".")[-1]
        unique_filename = f"{uuid.uuid4()}.{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        image = Image.open(file_path).convert("RGB")

        # Log checkpoint
        print("📸 Image saved and loaded.")

        caption = generate_caption(image)
        print("📝 Caption generated:", caption)

        detected_objects = detect_object(file_path)
        print("📦 Objects detected:", detected_objects)

        extracted_text = extract_text_from_image(file_path)
        print("🔤 OCR Text extracted:", extracted_text)

        full_message = f"{caption}. Detected: {', '.join(detected_objects)}."
        if extracted_text:
            full_message += f" Also, the image contains this text: {extracted_text}"

        audio_url = text_to_speech(full_message)
        print("🔊 Audio generated:", audio_url)

        return {
            "caption": caption,
            "detected_objects": detected_objects,
            "ocr_text": extracted_text,
            "audio_url": audio_url
        }

    except Exception as e:
        import traceback
        traceback.print_exc()  # Log detailed traceback
        return JSONResponse(status_code=500, content={"error": str(e)})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
