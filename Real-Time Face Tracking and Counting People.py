import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam")
    exit()
print("Press 'q' to quit the program.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale( gray , scaleFactor = 1.2 , minNeighbors = 5 , minSize = (40 , 40))
    for ( x , y , w , h ) in faces:
        cv2.rectangle(frame , ( x ,y) , ( x + w , y + h ) , ( 0 , 255 , 0 ) , 2 )
        face_count = len(faces)
        cv2.putText( frame , f"People Count: {face_count}" , ( 10 , 30 ) , cv2.FONT_HERSHEY_SIMPLEX , 1 , ( 0 , 255 , 0 ) , 2 )
    cv2.imshow("Real Time Face Tracking and Counting People" , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()