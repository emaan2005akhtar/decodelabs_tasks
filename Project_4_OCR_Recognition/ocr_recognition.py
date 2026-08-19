import cv2
import pytesseract
from pathlib import Path


# Tesseract OCR engine path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Project paths
BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "sample" / "sample_text.png"
OUTPUT_PATH = BASE_DIR / "output" / "processed_image.png"


def main():
    # Check whether sample image exists
    if not IMAGE_PATH.exists():
        print("Error: sample_text.png was not found.")
        print(f"Please place the image here: {IMAGE_PATH}")
        return

    # Read image
    image = cv2.imread(str(IMAGE_PATH))

    if image is None:
        print("Error: Could not read the image.")
        return

    # Step 1: Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 3: Adaptive thresholding
    thresholded = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Save processed image for visual confirmation
    cv2.imwrite(str(OUTPUT_PATH), thresholded)

    # Step 4: OCR text extraction
    text = pytesseract.image_to_string(
        thresholded,
        config="--psm 6"
    )

    # Step 5: OCR confidence calculation
    data = pytesseract.image_to_data(
        thresholded,
        config="--psm 6",
        output_type=pytesseract.Output.DICT
    )

    confidence_values = []

    for confidence in data["conf"]:
        try:
            value = float(confidence)

            if value >= 0:
                confidence_values.append(value)
        except ValueError:
            pass

    average_confidence = (
        sum(confidence_values) / len(confidence_values)
        if confidence_values
        else 0
    )

    print("=" * 60)
    print("       PROJECT 4 - OCR IMAGE RECOGNITION")
    print("=" * 60)

    print("\nPre-processing:")
    print("✓ Grayscale conversion")
    print("✓ Gaussian blur")
    print("✓ Adaptive thresholding")

    print("\nRecognized Text:")
    print("-" * 60)

    if text.strip():
        print(text.strip())
    else:
        print("No text detected.")

    print("-" * 60)

    print(f"\nOCR Confidence: {average_confidence:.2f}%")

    if average_confidence >= 80:
        print("Validation: PASSED ✓")
        print("Confidence is above the required 80% threshold.")
    else:
        print("Validation: BELOW 80%")
        print("Try using a clearer image with larger, darker text.")

    print(f"\nProcessed image saved at:")
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()