import os
import shutil

# 최상위 폴더 경로를 지정하세요.
base_directory = "C:\Users\Recorder\Desktop\rtsp - 복사본"

source_directory = "C:\Users\Recorder\Desktop\1"

# 폴더 번호 범위 지정
start_folder = 7001
end_folder = 7066

# 파일 이름 설정
source_file_name1 = "main.mp4"
source_file_name2 = "sub.mp4"
destination_file_name1 = "main.mp4"
destination_file_name2 = "sub.mp4"

for folder_number in range(start_folder, end_folder + 1):
    folder_path = os.path.join(base_directory, str(folder_number))  # 폴더 경로 생성
    source_file_path1 = os.path.join(source_directory, source_file_name1)  # 복사할 원본 파일 경로
    source_file_path2 = os.path.join(source_directory, source_file_name2)  # 복사할 원본 파일 경로
    destination_file_path1 = os.path.join(folder_path, destination_file_name1)  # 복사될 파일 경로
    destination_file_path2 = os.path.join(folder_path, destination_file_name2)  # 복사될 파일 경로

    # 폴더가 존재하는지 확인
    if os.path.exists(folder_path):
        try:
            # 파일 복사
            shutil.copy2(source_file_path1, destination_file_path1)
            print(f"Copied to {folder_path}")
            shutil.copy2(source_file_path2, destination_file_path2)
            print(f"Copied to {folder_path}")
        except Exception as e:
            print(f"Failed to copy to {folder_path}: {e}")
    else:
        print(f"Folder does not exist: {folder_path}")
