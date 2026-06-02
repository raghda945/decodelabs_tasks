# OCR Text Recognition Project

## Project Overview

This project demonstrates Optical Character Recognition (OCR) using Python, OpenCV, and Tesseract OCR. The system reads text from images and converts it into editable digital text.

## Objectives

* Extract text from images.
* Apply image preprocessing techniques.
* Improve text recognition accuracy.
* Display the detected text clearly.

## Technologies Used

* Python
* OpenCV
* Pytesseract
* Tesseract OCR

## Project Structure

```
OCR_Project/
│
├── images/
│   ├── sc1.png
│   ├── sc2.png
│   └── sc3.png
│
├── ocr.py
├── README.md
└── requirements.txt
```

## Installation

Install the required libraries:

```bash
pip install opencv-python pytesseract
```

Install Tesseract OCR and configure its path in the Python code.

## How It Works

1. Load an image.
2. Convert the image to grayscale.
3. Apply thresholding to enhance text visibility.
4. Use Tesseract OCR to extract text.
5. Display the recognized text.

## Sample Code

```python
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("sc1.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(thresh)

print(text)
```

## Results

The system successfully extracts text from image files and displays the recognized content in the terminal.

## Future Improvements

* Support Arabic OCR.
* Improve preprocessing techniques.
* Create a graphical user interface (GUI).
* Process multiple images automatically.

## Author

Raghda Samy
