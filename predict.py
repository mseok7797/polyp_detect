from ultralytics import YOLO
import torch
import os
from PIL import Image
from datetime import datetime

# 모델 로딩
model_path = "runs/detect/yolo_n_300e2" # 사용할 학습 결과물 폴더 
model = YOLO(os.path.join(model_path, "weights","best.pt"))

# GPU 사용 설정
torch.cuda.set_device(0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device=device)

# 테스트할 이미지 목록
test_img_path = os.path.join('test','images')
images = [os.path.join(test_img_path,f) for f in os.listdir(test_img_path)]


if __name__ == '__main__':   
    # predict
    results = model(images)

    # 예측 결과 이미지 저장할 폴더 생성
    current_dt = datetime.now().strftime("%y%m%d_%H%M%S")
    output_path = os.path.join('results', current_dt)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 이미지 저장
    for result in results:
        filename = os.path.basename(result.path)
        output = os.path.join(output_path, filename)
        
        for r in result:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            im.save(output)  # save image