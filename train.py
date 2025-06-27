
''''''
from ultralytics import YOLO
import torch

# 모델 로딩
model = YOLO('yolov8l.pt')

# GPU 사용 설정
torch.cuda.set_device(0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device=device)


if __name__ == '__main__':
   epochs = 400

   # Training.
   results = model.train(
      data='colon.yaml',
      imgsz=640,
      epochs=epochs,
      batch=2,
      patience=80,
      augment=True,
      optimizer='Adam',
      conf = 0.7,             # 0.7>=바운딩 박스를 예측, precision up/recall down/false positive down
      # max_det = 2,          # obj detect max num.
      lr0=1e-4,               # start learning rate
      warmup_bias_lr=1e-2,    # warming up stage bias 파라미터. 높을수록 데이터 분포 반영  
      lrf=5e-4,               # 최종 학습률 = (lr0 * lrf)
      ###
      
      erasing=0,
      name=f'yolov8l_polypPNG7.4_{epochs}e'
   )

'''   lr0 = 0.00535,
      lrf = 0.01093,
      momentum = 0.95115,
      weight_decay = 0.00036,
      warmup_epochs = 2.69727,
      warmup_momentum = 0.69637,
      box= 8.36667,
      cls= 0.6074,
      dfl= 1.75319,
      hsv_h= 0.01632,
      hsv_s= 0.53856,
      hsv_v= 0.34426,
      degrees= 0.0,
      translate= 0.10456,
      scale= 0.42282,   
      shear= 0.0,
      perspective= 0.0,
      flipud= 0.0,
      fliplr= 0.39765,
      bgr= 0.0,
      mosaic= 0.87808,
      mixup= 0.0,
      copy_paste= 0.0,
      warmup_bias_lr=0.05,
      '''


'''
# 중단된 작업 재시작

if __name__ == '__main__':
   from ultralytics import YOLO
   import torch

   model = YOLO("runs/detect/yolov8m_polypPNG7.4_400e2/weights/last.pt")  

   # Resume training
   results = model.train(resume=True, workers=0)

'''
