from gtts import gTTS
import os
import uuid

def text_to_speech(text: str, output_dir="static/audio"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(output_dir, filename)

    tts = gTTS(text)
    tts.save(filepath)

    return f"/{filepath.replace(os.sep, '/')}"  # returns relative URL path
