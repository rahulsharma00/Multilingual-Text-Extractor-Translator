# Multilingual-Text-Extractor-Translator

This is a `Streamlit`-based web application that allows users to extract text from images and translate the extracted text into English (if the text is in another language). The application supports two languages: English and Hindi. It uses `EasyOCR` for text extraction and `Google Translator` for translation.

Features
Text Extraction:

Extract text from images using Optical Character Recognition (OCR).

Supports English and Hindi languages.

Text Translation:

Automatically translate extracted text into English if the selected language is Hindi.

Dynamic Folder Creation:

Every time the app is executed, a new folder is created inside a parent folder named texts.

Folders are named incrementally (e.g., folder1, folder2, etc.).

Each folder contains two files:

extracted_text.txt: Contains the extracted text.

translated_text.txt: Contains the translated text (if applicable).

User-Friendly Interface:

Simple and intuitive interface built with Streamlit.

Users can upload an image and select the language of the text in the image.

Error Handling:

Handles errors during OCR and translation processes gracefully, displaying appropriate error messages to the user.
