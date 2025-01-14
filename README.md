
# Multilingual Text Extractor & Translator

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![EasyOCR](https://img.shields.io/badge/EasyOCR-00BFFF?style=for-the-badge)
![Google Translate](https://img.shields.io/badge/Google_Translate-4285F4?style=for-the-badge&logo=google-translate&logoColor=white)

This is a **Streamlit-based web application** that allows users to extract text from images and translate the extracted text into English (if the text is in another language). The application supports two languages: **English** and **Hindi**. It uses **EasyOCR** for text extraction and **Google Translator** for translation.

---

## Features

- **Text Extraction**:
  - Extract text from images using Optical Character Recognition (OCR).
  - Supports English and Hindi languages.

- **Text Translation**:
  - Automatically translate extracted text into English if the selected language is Hindi.

- **Dynamic Folder Creation**:
  - Each execution creates a new folder inside a parent folder named `texts`.
  - Folders are named incrementally (e.g., `folder1`, `folder2`, etc.).

- **Save Results**:
  - Each folder contains:
    - `extracted_text.txt`: Contains the extracted text.
    - `translated_text.txt`: Contains the translated text (if applicable).

- **User-Friendly Interface**:
  - Simple and intuitive interface built with Streamlit.

- **Error Handling**:
  - Handles errors during OCR and translation processes gracefully.

---

## How It Works

1. **User Input**:
   - Upload an image (JPG, JPEG, or PNG).
   - Select the language of the text in the image (English or Hindi).

2. **Image Processing**:
   - The uploaded image is displayed for confirmation.

3. **Text Extraction**:
   - The `easyocr` library performs OCR on the image.
   - Extracted text is displayed in the app.

4. **Text Translation**:
   - If the selected language is Hindi, the text is translated into English using the `deep_translator` library.
   - Translated text is displayed in the app.

5. **Save Results**:
   - A new folder is created inside the `texts` folder.
   - Extracted and translated text are saved as `.txt` files.

6. **Error Handling**:
   - Displays warnings if no text is detected.
   - Displays error messages if OCR or translation fails.

---

## Example Workflow

- Upload an image containing text.
- Select the language of the text (e.g., Hindi).
- View the extracted text.
- View the translated text (if applicable).
- Results are saved in a new folder inside the `texts` folder.

---

## Folder Structure

After multiple executions, the folder structure will look like this:

```
texts/
├── folder1/
│   ├── extracted_text.txt
│   └── translated_text.txt
├── folder2/
│   ├── extracted_text.txt
│   └── translated_text.txt
├── folder3/
│   ├── extracted_text.txt
│   └── translated_text.txt
└── ...
```

---

## How to Run the App

### Prerequisites

- Python 3.7 or higher.
- Install the required libraries:

```bash
pip install streamlit pillow easyocr numpy deep-translator
```

### Steps

1. Clone the repository:

```bash
git clone https://github.com/your-username/multilingual-text-extractor.git
cd multilingual-text-extractor
```

2. Run the app:

```bash
streamlit run app.py
```

3. Open the provided URL in your browser to use the app.

---

## Example Output

- **First Execution**:
  ```
  Created folder: texts/folder1
  Extracted text saved to texts/folder1/extracted_text.txt
  Translated text saved to texts/folder1/translated_text.txt
  ```

- **Second Execution**:
  ```
  Created folder: texts/folder2
  Extracted text saved to texts/folder2/extracted_text.txt
  Translated text saved to texts/folder2/translated_text.txt
  ```

---

## Limitations

- **OCR Accuracy**: Depends on image quality and text complexity.
- **Language Support**: Currently supports only English and Hindi.
- **Translation Errors**: May fail if the extracted text is noisy or contains unsupported characters.

---

## Future Improvements

- Add support for more languages.
- Implement image preprocessing techniques to improve OCR accuracy.
- Allow batch processing of multiple images.
- Add functionality to save output in other formats (e.g., Word, PDF).

---

## Contribution

Contributions are welcome! If you'd like to contribute, please:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Screenshots
<img width="1437" alt="Screenshot 2025-01-14 at 11 37 20 AM" src="https://github.com/user-attachments/assets/851182c8-542b-4685-bc21-7826a6c9e6a7" />
<img width="1437" alt="Screenshot 2025-01-14 at 11 37 29 AM" src="https://github.com/user-attachments/assets/04bbfebb-5181-461b-9284-d4f4b4cf2d08" />

---

## Repository Structure

```
multilingual-text-extractor/
├── app.py                # Main Streamlit application code
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── texts/                # Parent folder to store all execution folders
```

---

This `README.md` is now structured with bullet points for better readability and organization. Let me know if you need further adjustments!
