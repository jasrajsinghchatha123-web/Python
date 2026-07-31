import cv2
image = cv2.imread("Image3.jpeg")
if image is None:
    print("Error: Image not found!")
    exit()
print("\n===== IMAGE EDITOR =====")
print("1. Rotate Image")
print("2. Crop Image")
print("3. Increase Brightness")
print("4. Decrease Brightness")
print("5. Exit")
choice = int(input("Enter your choice (1-5): "))
if choice == 1:
    angle = float(input("Enter rotation angle (in degrees): "))
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    result = cv2.warpAffine(image, matrix, (w, h))
    cv2.imshow("Rotated Image", result)
    cv2.imwrite("rotated.jpg", result)
elif choice == 2:
    print("Enter the crop coordinates.")
    x = int(input("Start X: "))
    y = int(input("Start Y: "))
    width = int(input("Width: "))
    height = int(input("Height: "))
    result = image[y:y+height, x:x+width]
    cv2.imshow("Cropped Image", result)
    cv2.imwrite("cropped.jpg", result)
elif choice == 3:
    value = int(input("Increase brightness by (e.g. 50): "))
    result = cv2.convertScaleAbs(image, alpha=1, beta=value)
    cv2.imshow("Brightened Image", result)
    cv2.imwrite("brightened.jpg", result)
elif choice == 4:
    value = int(input("Decrease brightness by (e.g. 50): "))
    result = cv2.convertScaleAbs(image, alpha=1, beta=-value)
    cv2.imshow("Darkened Image", result)
    cv2.imwrite("darkened.jpg", result)
elif choice == 5:
    print("Exiting...")
    exit()
else:
    print("Invalid choice!")
    exit()
print("Image saved successfully.")
cv2.waitKey(0)
cv2.destroyAllWindows()