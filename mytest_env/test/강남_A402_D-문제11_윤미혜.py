import cv2
import cv2.data

# Cascasde
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# 카메라
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # frame 회색으로 변경
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 인지하기
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=5)

    # 얼굴
    for (x, y, w, h) in faces:

        # 사각형 그리기
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # 입은 얼굴 안에서 찾기 위해 범위 재설정
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # 웃는 입 인지하기
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=25,
            minSize=(25,25)
        )
        # 웃는 입 그리기
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sw), (0, 255, 0), 2)
            cv2.putText(frame, "SMILE!", (sx, sy), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            break

    cv2.imshow("smile", frame)

    # 'q' 입력하면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
 




