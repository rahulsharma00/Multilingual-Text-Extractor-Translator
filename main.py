import streamlit as st
from PIL import Image
import easyocr
import numpy as np
from deep_translator import GoogleTranslator
import os
from datetime import datetime

# Parent folder to store all execution folders
PARENT_FOLDER = "texts"

# Create the parent folder if it doesn't exist
if not os.path.exists(PARENT_FOLDER):
    os.makedirs(PARENT_FOLDER)

# Function to create a new folder with an incremental name inside the parent folder
def create_new_folder():
    base_name = "folder"
    counter = 1
    while True:
        folder_name = os.path.join(PARENT_FOLDER, f"{base_name}{counter}")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            return folder_name
        counter += 1

st.title("Multilingual Text Extractor & Translator")

# Language selection
selected_language = st.selectbox("Select the language in the image:", ["English", "Hindi"])

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Streamlit theme customization (optional)
primaryColor = "#6eb52f"
backgroundColor = "#f0f0f5"
secondaryBackgroundColor = "#e0e0ef"
textColor = "#262730"
font = "sans serif"

if uploaded_file is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Initialize EasyOCR reader
    @st.cache_resource
    def get_reader(lang):
        return easyocr.Reader([lang], gpu=False)

    try:
        # Get the reader for the selected language
        reader = get_reader("en" if selected_language == "English" else "hi")
        
        # Perform OCR on the image
        result = reader.readtext(np.array(image))

        if result:
            # Extract text from the OCR result
            extracted_text = " ".join([text for _, text, _ in result])
            st.write(f"Extracted Text ({selected_language}):")
            st.code(extracted_text, language="text")

            # Translate the text if the selected language is not English
            translated_text = ""
            if selected_language != "English":
                try:
                    translated_text = GoogleTranslator(source='auto', target='en').translate(extracted_text)
                    st.write("Translated Text (English):")
                    st.code(translated_text, language="text")
                except Exception as e:
                    st.error(f"Translation error: {str(e)}")

            # Create a new folder for this execution inside the parent folder
            folder_name = create_new_folder()
            st.success(f"Created folder: {folder_name}")

            # Save extracted text to a file
            extracted_text_path = os.path.join(folder_name, "extracted_text.txt")
            with open(extracted_text_path, "w", encoding="utf-8") as file:
                file.write(extracted_text)
            st.success(f"Extracted text saved to {extracted_text_path}")

            # Save translated text to a file (if available)
            if translated_text:
                translated_text_path = os.path.join(folder_name, "translated_text.txt")
                with open(translated_text_path, "w", encoding="utf-8") as file:
                    file.write(translated_text)
                st.success(f"Translated text saved to {translated_text_path}")

        else:
            st.warning("No text detected.")
    except Exception as e:
        st.error(f"OCR error: {str(e)}")