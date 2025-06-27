import os
import cv2
from ultralytics import solutions

# 파일명 유지
# 이미지 폴더 경로와 결과 저장 폴더 설정
image_dir = "../datasets/polypPNG_7.4/test/images"              # ../datasets/polypPNG_7.4/train (1,2,3,6,7,9,10) or test&valid (4,5,8)
output_dir = "yolov8m_cropped_polyp_test"

# 결과 저장 폴더가 없으면 생성
os.makedirs(output_dir, exist_ok=True)

# ObjectCropper 초기화
cropper = solutions.ObjectCropper(
    show=False,                # 결과를 실시간으로 출력할 필요가 없으면 False로 설정 (True로 설정하면 창이 뜹니다)
    model="yolov8m_polypPNG7.4_best.pt",   # 학습된 가중치 파일
    classes=[0],              # 감지할 클래스 (필요에 따라 조정)
    conf=0.5,                  # 감지 신뢰도 임계값
    crop_dir=output_dir,       # 크롭된 결과가 저장될 폴더
)

# 이미지 폴더 내의 모든 이미지 파일(PNG, JPG, JPEG) 목록 생성
image_files = [
    os.path.join(image_dir, f)
    for f in os.listdir(image_dir)
    if f.lower().endswith(('.png', '.jpg', '.jpeg'))
]

print(f"총 {len(image_files)}개의 이미지 파일을 찾았습니다. 크롭을 시작합니다...")

# 각 이미지에 대해 객체 감지 및 크롭 작업 수행(수정정)
for img_path in image_files:
    try:
        # 이미지를 cv2로 읽어서 numpy array로 로드
        img = cv2.imread(img_path)
        if img is None:
            print("이미지 로드 실패:", img_path)
            continue
        
        # 작업 전 output 폴더 내의 파일 목록 저장
        before_files = set(os.listdir(output_dir))
        
        # 크롭 작업 수행: 이미지 array를 직접 전달합니다.
        results = cropper(img)
        
        # 작업 후 output 폴더 내의 새 파일 목록 파악
        after_files = set(os.listdir(output_dir))
        new_files = list(after_files - before_files)
        
        if not new_files:
            print("크롭 결과가 없습니다:", img_path)
        else:
            # 원본 이미지의 base name 추출 (확장자 제외)
            original_base = os.path.splitext(os.path.basename(img_path))[0]
            new_files_sorted = sorted(new_files)  # 정렬하여 순서를 고정
            # 새로 생성된 파일이 1개라면 원본 파일명과 동일하게, 여러 개면 번호를 붙임.
            for i, new_file in enumerate(new_files_sorted):
                old_path = os.path.join(output_dir, new_file)
                ext = os.path.splitext(new_file)[1]
                # 확장자가 .png인 경우 대문자로 .PNG로 지정
                if ext.lower() == '.PNG':
                    ext = '.PNG'
                if len(new_files_sorted) == 1:
                    new_name = original_base + ext
                else:
                    new_name = f"{original_base}_{i+1}{ext}"
                new_path = os.path.join(output_dir, new_name)
                os.rename(old_path, new_path)
                print(f"파일 이름 변경: {old_path} -> {new_path}")
        
        print(f"처리 완료: {os.path.basename(img_path)}")

    except Exception as e:
        print(f"이미지 처리 중 오류 발생: {img_path} - {e}")

print(f"모든 이미지 크롭 작업이 완료되었습니다!")

# 각 이미지에 대해 객체 감지 및 크롭 수행(원본)
'''
for img_path in image_files:
    try:
        # ObjectCropper 객체를 직접 호출하여 처리 (원래 results = cropper.crop 메서드 대신)
        results = cropper(source=img_path)
        print(f"처리 완료: {os.path.basename(img_path)}")
    except Exception as e:
        print(f"이미지 처리 중 오류 발생: {img_path} - {e}")

print("모든 이미지 크롭 작업이 완료되었습니다!")
'''

''' 

# 영상 파일 경로 (필요에 따라 수정)
video_path = "../resources/polyp_test_vid_raw/test1/output_raw.avi"  # 영상 파일 경로(지금 resources에 없음)
cap = cv2.VideoCapture(video_path)
assert cap.isOpened(), "Error reading video file"

# 크롭 결과 저장 폴더 생성
output_dir = "cropped-polyp"
os.makedirs(output_dir, exist_ok=True)

# ObjectCropper 초기화 (yolo11n_best.pt 기반)
cropper = solutions.ObjectCropper(
    show=True,                # 처리된 프레임을 화면에 출력 (False로 설정하면 출력하지 않음)
    model="yolo11n_best.pt",  # 사용 모델 지정
    classes=[0],              # 감지할 클래스 (필요시 조정)
    conf=0.5,                 # 감지 신뢰도 임계값
    crop_dir=output_dir,      # 크롭된 결과 저장 폴더
)

# 영상 처리 루프
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break

    # 프레임에 대해 객체 감지 및 크롭 작업 수행
    results = cropper(frame)
    
    # 결과 출력 후 1ms 대기, 'q' 키 입력 시 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''