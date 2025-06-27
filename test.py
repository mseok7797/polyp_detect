'''from datetime import datetime

print(datetime.now().strftime("%y%m%d_%H%M%S"))'''

import os
from ultralytics import YOLO
import torch
import cv2

# model load
model_path = os.path.join('runs','detect','yolov8n_polyp1_300e2')
model = YOLO(os.path.join(model_path, "weights","best.pt"))

# GPU 사용 설정
torch.cuda.set_device(0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device='cpu')

results = model.predict("../resource/polyp_test_PNG_relabeled_blur_del/test/images", save_json = True)



