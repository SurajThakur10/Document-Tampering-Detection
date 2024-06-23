# Document Tampering Detection

![App Screenshot](https://png.pngtree.com/png-vector/20220519/ourmid/pngtree-business-documents-scanning-market-analysis-png-image_4711698.png)

Document Tampering Detection is a web application that allows users to detect whether a document has been tampered with by comparing the original and tampered images.

## Overview

Document tampering is a common issue, especially in scenarios where official documents like IDs, passports, or certificates need to be verified for authenticity. This project aims to provide a simple and efficient way to detect tampering in documents using Structural Similarity Index (SSIM) metric.

## Features

- **Image Upload**: Users can upload the original and tampered images from their local storage.
- **Real-Time Analysis**: The application provides real-time analysis of uploaded images to determine if the document is tampered.
- **SSIM Score Display**: Displays the SSIM score, which quantifies the similarity between the original and tampered images.
- **Result Indication**: Indicates whether the document is tampered based on the SSIM score.

## Usage

To use the application, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/SurajThakur10/Document-Tampering-Detection.git

2. Navigate to the project directory:

   ```bash
   cd document-tampering-detection

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

4. Run the Flask application:

   ```bash
   python app.py
5. Open your web browser and go to http://localhost:5000 to access the application.
6. Upload the original and tampered images from your local storage.
7. Click the "Submit" button to analyze the images.
8. The application will display the SSIM score and indicate whether the document is tampered.

## Dependencies

- **Flask**: Web framework for Python.
- **scikit-image**: Image processing library for Python.
- **OpenCV**: Computer vision library for Python.
- **Result Indication**: Indicates whether the document is tampered based on the SSIM score.

## Contributing

Contributions to the project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/SurajThakur10/Document-Tampering-Detection/blob/master/LICENSE) file for details.










