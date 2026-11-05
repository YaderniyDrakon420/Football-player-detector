from ultralytics import YOLO
import cv2

# Завантажуємо навчену модель
model = YOLO("./runs/detect/train-2/weights/best.pt")

# Передаємо зображення моделі
img = input("Enter image name: ")
results = model.predict(
    source=f"./assets/{img}",
    conf=0.25
)

# Отримуємо результат
result = results[0]

# Малюємо рамки навколо знайдених об'єктів
image = result.plot()

# Показуємо зображення
cv2.imshow("YOLO Football", image)

cv2.waitKey(0)
cv2.destroyAllWindows()