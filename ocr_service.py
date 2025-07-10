import easyocr
from PIL import Image
import numpy as np

reader = easyocr.Reader(['en'])  # Add more languages if needed

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    image_np = np.array(image)
    results = reader.readtext(image_np)

    extracted_text = ' '.join([res[1] for res in results])
    return extracted_text
