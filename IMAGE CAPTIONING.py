import cv2
import pytesseract

def perform_ocr(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        text = pytesseract.image_to_string(thresh)
        return True, text.strip()  
    except Exception as e:
        return False, str(e)

def main():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Unable to open camera.")
        return

    print("Camera opened successfully.")
    ret, frame = camera.read()
    if not ret:
        print("Error: Unable to capture frame.")
        camera.release()
        return

    print("Frame captured successfully.")
    success, text = perform_ocr(frame)
    if success:
        print("OCR performed successfully.")
        print("Recognized text:")
        print(text)
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imwrite("scan_image.jpg", frame)
        print("Frame with recognized text saved as 'scan_image.jpg'")
    else:
        print("Error occurred during OCR:", text)
    camera.release()
    print("Camera released.")

if _name_ == "_main_":
    main()