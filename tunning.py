from ultralytics import YOLO
import torch

# 모델 로딩
model = YOLO('yolov8m.pt')

# GPU 사용 설정
torch.cuda.set_device(0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device=device)

# Tune hyperparameters on polypPNG7.4 for 30 epochs
model.tune(data='colon.yaml',
           epochs=50, 
           iterations=100, 
           workers=8,
           optimizer="Adam",
           erasing=0,
           name='yolov8m_polypPNG7.4_tune',
           plots=False, 
           save=False, 
           val=False)