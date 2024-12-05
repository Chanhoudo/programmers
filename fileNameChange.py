import os

def rename_specific_files_in_folders(parent_folder_path, start_folder, end_folder):
    try:
        # 주어진 범위 내의 폴더들에 대해 작업을 수행합니다
        for folder_num in range(start_folder, end_folder + 1):
            folder_path = os.path.join(parent_folder_path, str(folder_num))
            
            # 폴더가 존재하는지 확인합니다
            if not os.path.exists(folder_path):
                print(f"{folder_path} 경로가 존재하지 않습니다.")
                continue

            # 폴더 안의 파일 목록을 가져옵니다
            files = os.listdir(folder_path)
            
            # 파일들을 하나씩 순회하며 지정된 이름을 변경합니다
            for file_name in files:
                # 기존 파일 경로 설정
                old_file_path = os.path.join(folder_path, file_name)

                # "M.mp4" 파일을 "2M.mp4"로 변경
                if file_name == "M.mp4":
                    new_file_name = "2M.mp4"
                    new_file_path = os.path.join(folder_path, new_file_name)
                    os.rename(old_file_path, new_file_path)
                    print(f"{old_file_path} -> {new_file_path} 변경 완료.")
                
                # "S.mp4" 파일을 "2S.mp4"로 변경
                elif file_name == "S.mp4":
                    new_file_name = "2S.mp4"
                    new_file_path = os.path.join(folder_path, new_file_name)
                    os.rename(old_file_path, new_file_path)
                    print(f"{old_file_path} -> {new_file_path} 변경 완료.")

    except Exception as e:
        print(f"오류 발생: {e}")

# 예시 사용법
parent_folder_path = r"C:\Users\yunch\Downloads\OneDrive_2024-12-05 (1)"  # 부모 폴더 경로
start_folder = 7003  # 시작 폴더 번호
end_folder = 7064    # 끝 폴더 번호

rename_specific_files_in_folders(parent_folder_path, start_folder, end_folder)
