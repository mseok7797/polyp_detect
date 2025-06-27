import os
from ultralytics import YOLO
import torch

"""
yolo task=detect 
mode=val 
model=runs/detect/yolov8m_v8_50e/weights/best.pt 
name=yolov8m_eval 
data=pothole_v8.yaml 
imgsz=1280


"""

# 모델 로딩
#model = YOLO('yolov8l.pt')
model_path = os.path.join('runs','detect','yolov8n_polyp1_300e2')
model = YOLO(os.path.join(model_path, "weights","best.pt"))

# GPU 사용 설정
torch.cuda.set_device(0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device='cpu')


if __name__ == '__main__':
    metrics = model.val(
        name='yolov8n300e2_val',
        save_json=True
    )
    print(metrics)
