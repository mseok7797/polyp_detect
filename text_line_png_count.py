import os

def count_lines_in_files(folder_path):
    total_lines = 0
    # 폴더와 하위 폴더 내의 파일 탐색
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith('.txt'):  # .txt 파일만 처리
                file_path = os.path.join(dirpath, filename)
                # 파일 열기 (UTF-8 인코딩, 에러 무시)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    lines = file.readlines()
                    total_lines += len(lines)
    return total_lines

def count_png_files(folder_path):
    count = 0
    # 폴더와 하위 폴더 내의 파일 탐색
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            # 파일 확장자가 .png (대소문자 무관)인 경우 카운트 증가
            if filename.lower().endswith('.png'):
                count += 1
    return count

# 지정한 폴더 경로 (올바른 경로 구분자 사용)
folder_path = "../resource/polyp_test_PNG_relabeled_blur_del"

# 각각의 함수 호출 후 결과 출력
total_lines = count_lines_in_files(folder_path)
total_png_files = count_png_files(folder_path)

print(f"Total number of lines in text files: {total_lines}")
print(f"Total number of PNG files: {total_png_files}")