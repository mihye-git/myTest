import cv2
import numpy as np

# 트랙바 사용시 필요한 콜백함수
def nothing(x):
    pass

# 이미지 경로 지정
imagePath = r"C:\Mytest\mytest_env\test\box_bgy1.png"

# 이미지 변환 (HSV)
img = cv2.imread(imagePath)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 트랙바 창 설정
trackbarTitle = "MyTrackbar"
cv2.namedWindow(trackbarTitle, cv2.WINDOW_NORMAL)
cv2.resizeWindow(trackbarTitle, 600, 1000)

# 트랙바 생성하기
cv2.createTrackbar("h_low", trackbarTitle, 0, 179, nothing)
cv2.createTrackbar("s_low", trackbarTitle, 0, 255, nothing)
cv2.createTrackbar("v_low", trackbarTitle, 0, 255, nothing)
cv2.createTrackbar("h_high", trackbarTitle, 179, 179, nothing)
cv2.createTrackbar("s_high", trackbarTitle, 255, 255, nothing)
cv2.createTrackbar("v_high", trackbarTitle, 255, 255, nothing)

while True:
    # 트랙바 값 설정
    h_low = cv2.getTrackbarPos("h_low", trackbarTitle)
    s_low = cv2.getTrackbarPos("s_low", trackbarTitle)
    v_low = cv2.getTrackbarPos("v_low", trackbarTitle)
    h_high = cv2.getTrackbarPos("h_high", trackbarTitle)
    s_high = cv2.getTrackbarPos("s_high", trackbarTitle)
    v_high = cv2.getTrackbarPos("v_high", trackbarTitle)

    # 범위 설정
    lower = np.array([h_low, s_low, v_low])
    upper = np.array([h_high, s_high, v_high])

    # 마스크 생성
    mask = cv2.inRange(hsv, lower, upper)

    # 마스크로 색상 필터링
    filter = cv2.bitwise_and(img, img, mask=mask)

    # 윤곽선 검출
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 사각형으로 그리기
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(filter, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # 결과 출력
    cv2.imshow(trackbarTitle, filter)

    # 'q'누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()

