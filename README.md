# AI Object Measurement System

## Overview

The AI Object Measurement System is a computer vision application that detects objects within an uploaded image and estimates their physical dimensions. The system processes the image using image processing techniques to identify object contours and calculate measurements such as width and height.

This project demonstrates how computer vision can be applied to automate measurement tasks that traditionally require manual tools. It can be used as a foundation for applications in manufacturing inspection, quality control, inventory management, and automated analysis systems.

## Objectives

The primary objectives of this project are:

* To detect objects present in an uploaded image
* To calculate approximate object dimensions using image processing
* To display measurement results visually
* To provide a simple web interface for interaction with the measurement system

## Technologies Used

Python
Flask
OpenCV
NumPy
HTML
CSS

## System Architecture

The system follows a simple web-based architecture:

User Uploads Image
↓
Flask Web Application
↓
Image Processing Module
↓
Object Detection and Contour Analysis
↓
Measurement Calculation
↓
Result Display with Measured Dimensions

## Project Structure

AI_Object_Measurement

app.py
requirements.txt

templates/
 index.html
 result.html

static/
 css/
  style.css

uploads/

## Module Description

### app.py

The main Flask application that handles routing, image uploads, and integration with the measurement logic.

### templates/

Contains HTML templates used to render the web interface.

* **index.html** – Upload interface for submitting images
* **result.html** – Displays processed image and measurement results

### static/

Contains static resources such as CSS styles used for the user interface.

### uploads/

Stores uploaded images temporarily for processing.

## How the System Works

1. The user uploads an image through the web interface.
2. The Flask server receives and stores the image.
3. The image processing module reads the uploaded image.
4. OpenCV is used to detect object contours.
5. Measurements are estimated based on pixel distances.
6. The processed image and measurement results are displayed on the result page.

## Installation

Clone the repository:

git clone https://github.com/yourusername/AI_Object_Measurement.git

Navigate to the project directory:

cd AI_Object_Measurement

Install required dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open a browser and navigate to:

http://127.0.0.1:5000

## Applications

Object measurement systems have applications in multiple domains including:

Manufacturing inspection
Quality control systems
Warehouse automation
Packaging analysis
Research and academic demonstrations

## Limitations

Measurements are approximate and depend on image quality, camera angle, and calibration. Accurate real-world measurement may require a reference object or calibration process.

## Future Improvements

Possible improvements for the system include:

* Integration of deep learning-based object detection
* Real-world unit calibration using reference markers
* Support for measuring multiple objects simultaneously
* Improved user interface and visualization
* Integration with industrial inspection pipelines

## License

This project is intended for educational and research purposes.
