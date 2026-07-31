import cv2
import numpy as np
image = cv2.imread("Image3.jpeg")
if image is None:
    print("Error: Image not found")
    exit()
height , width = image.shape[:2]
center = (width // 2 , height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center , 45 , 1.0)
rotated_image = cv2.warpAffine(image , rotation_matrix , (width , height))
cropped_image = rotated_image[100:400 , 100:400]
brightness = 50
bright = cv2.convertScaleAbs(cropped_image , alpha = 1 , beta = brightness)
dark = cv2.convertScaleAbs(cropped_image , alpha = 1 , beta = -50)
cv2.imshow("Original Image" , image)
cv2.imshow("Rotated Image" , rotated_image)
cv2.imshow("Cropped Image" , cropped_image)
cv2.imshow("Brightened Image" , bright)
cv2.imshow("Darkened Image" , dark)
cv2.imwrite("Rotated_Image.jpg" , rotated_image)
cv2.imwrite("Cropped_Image.jpg" , cropped_image)
cv2.imwrite("Brightened_Image.jpg" , bright)
cv2.imwrite("Darkened_Image.jpg" , dark)
print("Image manipulation completed successfully.")
cv2.waitKey(0)
cv2.destroyAllWindows()