import cv2

# Global constants
THRESHOLD_VALUE = 127

def load_image(image_path):
    return cv2.imread(image_path)

def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def extract_contours(gray_image):
    _, thresholded = cv2.threshold(gray_image, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def display_contours(image, contours):
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'OpenCV.png'
    image = load_image(image_path)
    gray_image = convert_to_gray(image)
    contours = extract_contours(gray_image)
    display_contours(image, contours)
