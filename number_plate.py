import cv2
import easyocr
import matplotlib.pyplot as plt

# Load the image
image_path = 'car_image.jpg'  # Replace with the path to your image
img = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 170, 200)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Filter for number plate-sized contours
number_plate = None
for contour in contours:
    # Approximate the contour
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    if len(approx) == 4:  # If it has 4 sides, it's potentially a plate
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if 2 < aspect_ratio < 6:  # Aspect ratio of a license plate
            number_plate = gray[y:y + h, x:x + w]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Draw rectangle on plate
            break

# Display the image with the detected plate
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Detected Number Plate")
plt.show()

# If a plate was detected, apply OCR
if number_plate is not None:
    reader = easyocr.Reader(['en'])
    result = reader.readtext(number_plate)
    print("Detected Text:", result)
else:
    print("No number plate detected.")
