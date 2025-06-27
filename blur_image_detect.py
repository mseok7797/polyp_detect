import cv2
import os

'''

def is_blurry(image, threshold=100):
    """
    이미지의 선명도를 Laplacian 분산을 통해 계산합니다.
    분산이 threshold 미만이면 블러로 간주합니다.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var < threshold, laplacian_var

# 이미지가 저장된 폴더 경로 (필요에 따라 수정)
folder_path = '../resource/polyp_test_PNG_relabeled_blur_del/polyp_test_1_yolo'
# 블러 판별 임계값 (데이터 특성에 맞게 조정)
threshold_value = 100

# 폴더 내의 파일들을 순회
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.PNG')):
        file_path = os.path.join(folder_path, filename)
        image = cv2.imread(file_path)
        if image is None:
            continue  # 이미지 로드 실패 시 건너뜁니다.
        blurry, variance = is_blurry(image, threshold=threshold_value)
        if blurry:
            print(f"{filename} is blurry (Laplacian variance: {variance:.2f})")
            # 이미지 창에 띄우고 사용자가 키를 누를 때까지 대기
            cv2.imshow(f"Blurry Image: {filename}", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# 작업중단기능, 간편기능 등 추가

'''
# laplacian 분산값-최대최소평균- +히스토그램 추가하기


