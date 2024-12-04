import cv2
from deepface import DeepFace


def detect_and_estimate_age():
    # Kamerani ishga tushirish
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kamera ishga tushmadi!")
            break

        try:
            # DeepFace orqali analiz qilish
            result = DeepFace.analyze(frame, actions=['age'], enforce_detection=False)
            age = result['age']

            # Yuzni aniqlash va yoshni ko'rsatish
            cv2.putText(frame, f"Age: {int(age)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except Exception as e:
            print(f"Xato yuz berdi: {e}")

        # Tasvirni ko'rsatish
        cv2.imshow("Yoshni aniqlash", frame)

        # Tugmani bosib chiqish
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_and_estimate_age()
