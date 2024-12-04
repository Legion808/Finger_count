import cv2
import numpy as np

# Kamerani ishga tushiramiz
cap = cv2.VideoCapture(0)


def detect_fire(frame):
    # BGR formatidagi ramkani HSV formatiga o'tkazamiz
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Olovning HSV rang chegaralarini belgilaymiz
    lower_fire = np.array([18, 50, 50])  # Olovning pastki chegarasi
    upper_fire = np.array([35, 255, 255])  # Olovning yuqori chegarasi

    # Maskani hosil qilamiz
    mask = cv2.inRange(hsv, lower_fire, upper_fire)

    # Shovqinni kamaytirish uchun eroziya va kengaytirish
    mask = cv2.GaussianBlur(mask, (15, 15), 0)

    # Konturlarni aniqlaymiz
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Minimal maydon (odatda kichik shovqinlarni chiqarib tashlash uchun)
    min_area = 500

    # Agar konturlar mavjud bo'lsa, olovni aniqlaymiz
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > min_area:
            # Olovni o'rab turgan to'rtburchak yasaymiz
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Matnni chiqaramiz
            cv2.putText(frame, "Fire Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    return frame


while True:
    # Kameradan kadrni olamiz
    ret, frame = cap.read()
    if not ret:
        break

    # Olovni aniqlaymiz va ko'rsatamiz
    frame_with_fire = detect_fire(frame)

    # Natijani ko'rsatamiz
    cv2.imshow('Fire Detection', frame_with_fire)

    # 'q' tugmasi bosilganda chiqib ketish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerani to'xtatish
cap.release()
cv2.destroyAllWindows()
