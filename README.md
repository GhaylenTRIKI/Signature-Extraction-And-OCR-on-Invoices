# Signature-Extraction-And-OCR-on-Invoices</br>
1. Creation of a document scanner :</br>
+ Converts RGB image to gray</br>
+ Gaussian blur and canny filter to detect the contour</br>
+ A dilation to repair broken lines</br>
+ An erosion to refine separate objects</br>
+ Determine the largest contour and convert the coordinates to get the scanned image</br></br>
2. Separation of each box by a region (ROI) of the reference image</br>
3. A signature extraction module by determining the largest pixel connectivity</br>
4. Applying an optical character recognition (OCR) system using pytesseract</br>
5. The data extracted by the OCR will be saved in an excel file each in its appropriate box</br>
