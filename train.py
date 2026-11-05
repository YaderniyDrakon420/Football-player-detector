from ultralytics import YOLO
import torch

def main():
    print("CUDA:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
#n, s,m,l,x
    model = YOLO("weights.pt")

    results = model.train(
        data="./data.yaml",
        epochs=50,
        imgsz=416,
        batch=4,
        device=0, #cpu
        workers=0
    )

if __name__ == "__main__":
    main()


# yolo11n.pt — маленька модель.
#
#
#
# epochs=50 — 50 проходів по навчальній вибірці.
#
#
#
# imgsz=416 — розмір зображення.
#
#
#
# batch=4 — по 4 зображення за один крок.
#
#
#
# device=0 — NVIDIA T500.