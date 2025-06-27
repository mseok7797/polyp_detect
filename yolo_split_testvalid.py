import os
import random
import shutil
import sys

"""
이 파일을 사용할 수 있는 폴더구조 :

dataset             -> 루트 폴더. 사용자가 command line으로 전달. 폴더명 아무거나 상관X ex) python3 split.py dataset
├── images/         -> 이미지가 들어있는 폴더. 폴더명 images 여야함. 
│   ├── 1.jpg       -> 학습시킬 이미지파일. 확장자 : .jpg, .jpeg, .png, .bmp
│   ├── 2.jpg
│   ├── 3.jpg
│       ...
├── labels/         -> 레이블이 들어있는 폴더. 폴더명 labels 여야함.
│   ├── 1.txt       -> 학습시킬 yolo 포맷 레이블 파일. 확장자 : .txt
│   ├── 2.txt
│   ├── 3.txt
│       ...

결과물 폴더구조 :

dataset             
├── images/ 
├── labels/ 
├── output/      
│   ├── test/
│   │   ├── images/
│   │   │   ├── 1.jpg/
│   │   │       ...
│   │   ├── labels/
│   │   │   ├── 1.txt/
│   │   │       ...
│   ├── eval/

"""

# Constants =================================
LABEL_EXTENSIONS = ['.txt']
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.PNG', '.bmp']

EVAL_RATIO = 0.5
TEST_RATIO = 0.5

OUTPUT_EVAL_FOLDER = 'eval'
OUTPUT_TEST_FOLDER = 'test'
# ===========================================

def run(root_path):
    # 필요한 폴더 경로
    original_image_path = os.path.join(root_path, 'images')  # 원본 이미지 폴더
    original_label_path = os.path.join(root_path, 'labels')  # 원본 레이블 폴더
    output_path = os.path.join(root_path, 'output')          # 저장할 output 폴더

    # 이미지, 레이블 파일 리스트 생성
    image_list = get_filename_list(path=original_image_path, extensions=IMAGE_EXTENSIONS)
    label_list = get_filename_list(path=original_label_path, extensions=LABEL_EXTENSIONS)
    print(f'이미지 수 : {len(image_list)} | 레이블 수 : {len(label_list)}')

    # 이미지 랜덤하게 셔플
    random.shuffle(image_list)

    # output 폴더 생성
    create_output_folder(output_path=output_path)

    split_files(image_list=image_list,
                label_list=label_list,
                original_image_path=original_image_path,
                original_label_path=original_label_path,
                output_path=output_path)

def get_filename_list(path, extensions):
    file_list = [filename for filename in os.listdir(path) 
                 if os.path.splitext(filename)[-1] in extensions and filename != 'classes.txt']
    return file_list

def create_output_folder(output_path):
    eval_path = os.path.join(output_path, OUTPUT_EVAL_FOLDER)
    test_path = os.path.join(output_path, OUTPUT_TEST_FOLDER)

    for folder_path in [eval_path, test_path]:
        for subfolder in ['images', 'labels']:
            os.makedirs(os.path.join(folder_path, subfolder), exist_ok=True)

def split_files(image_list, label_list, output_path, original_image_path, original_label_path):
    # eval, test 몇 장씩 할지 계산
    eval_size = int(len(image_list) * EVAL_RATIO)
    test_size = len(image_list) - eval_size
    print(f'eval {eval_size} | test {test_size}')

    # output 폴더명
    eval_path = os.path.join(output_path, OUTPUT_EVAL_FOLDER)
    test_path = os.path.join(output_path, OUTPUT_TEST_FOLDER)

    for i, img_file in enumerate(image_list):
        # eval, test 중 어디에 넣을지 지정
        dest_folder = eval_path if i < eval_size else test_path

        # 현재 이미지파일과 같은 이름의 텍스트파일 (ex. 1.jpg -> 1.txt)
        filename = os.path.splitext(img_file)[0]
        txt_file = filename + '.txt'

        # 파일 복사
        img_file_path = os.path.join(original_image_path, img_file)
        txt_file_path = os.path.join(original_label_path, txt_file)
        if os.path.exists(img_file_path) and os.path.exists(txt_file_path):
            shutil.copy(img_file_path, os.path.join(dest_folder, "images", img_file))
            shutil.copy(txt_file_path, os.path.join(dest_folder, "labels", txt_file))

if __name__ == "__main__":
    # 커맨드라인에서 argument로 데이터 폴더 받기
    args = sys.argv[1:]
    if len(args) == 0:
        print("데이터 경로 미입력")
        exit()
    elif not os.path.isdir(args[0]):
        print('디렉토리가 아님')
        exit()
    root_dir = os.path.abspath(args[0])

    run(root_dir)