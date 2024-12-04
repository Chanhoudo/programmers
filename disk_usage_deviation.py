import wmi
import tkinter as tk
from tkinter import messagebox

# D 드라이브 사용량 가져오기 함수
def get_drive_usage(drive_letter):
    c = wmi.WMI()
    for disk in c.Win32_LogicalDisk():
        if disk.DeviceID == drive_letter:
            used = int(disk.Size) - int(disk.FreeSpace)
            total = int(disk.Size)
            free = int(disk.FreeSpace)
            return used, total, free
    return None, None, None

# 편차율 계산 함수
def calculate_deviation():
    try:
        # 텍스트 상자에서 하드디스크 개수 가져오기
        num_disks = int(disk_count_entry.get().strip())
        
        # 사용 가능한 디스크 정보 가져오기 (로컬 디스크 C 제외)
        drive_letters = ["D:", "E:", "F:", "G:", "H:", "I:"]
        selected_drives = drive_letters[:num_disks]
        
        if not selected_drives:
            messagebox.showerror("오류", "사용 가능한 디스크 정보를 찾을 수 없습니다.")
            print("오류: 사용 가능한 디스크 정보를 찾을 수 없습니다.")
            return
        
        usage_values = []
        for drive in selected_drives:
            used, total, free = get_drive_usage(drive)
            if used is not None:
                usage_values.append(used)
                print(f"{drive} 사용량: {used / (1024**3):.2f} GB")
            else:
                print(f"{drive}에 접근할 수 없습니다.")

        if len(usage_values) == 0:
            messagebox.showerror("오류", "사용 가능한 디스크 정보를 찾을 수 없습니다.")
            print("오류: 사용 가능한 디스크 정보를 찾을 수 없습니다.")
            return

        # 1. 평균 값 계산
        mean_value = sum(usage_values) / len(usage_values)

        # 2. 각 사용량과 평균의 차이 계산
        individual_deviations = [value - mean_value for value in usage_values]

        # 3. 편차 제곱 계산
        squared_deviations = [(dev) ** 2 for dev in individual_deviations]

        # 4. 분산 계산 (편차 제곱 값의 평균)
        variance = sum(squared_deviations) / len(usage_values)

        # 5. 표준 편차 계산
        std_dev = variance ** 0.5

        # 6. 편차율 계산 (표준 편차 / 평균 * 100)
        deviation_rate = (std_dev / mean_value) * 100

        # 결과 출력
        result = f"평균 사용량: {mean_value / (1024**3):.2f} GB\n표준 편차: {std_dev / (1024**3):.2f} GB\n편차율: {deviation_rate:.2f}%"
        messagebox.showinfo("계산 결과", result)
    except ValueError:
        messagebox.showerror("입력 오류", "올바른 숫자 형식으로 입력하세요 (하드디스크 개수는 정수로 입력하십시오)")
        print("입력 오류: 올바른 숫자 형식으로 입력하세요 (하드디스크 개수는 정수로 입력하십시오)")

# GUI 애플리케이션 설정
def create_app():
    root = tk.Tk()
    root.title("하드디스크 편차율 계산기")
    root.geometry("400x300")

    # 하드디스크 개수 입력 안내 레이블
    disk_count_label = tk.Label(root, text="하드디스크 개수를 입력하세요:")
    disk_count_label.pack(pady=5)

    # 하드디스크 개수 입력 텍스트 상자
    global disk_count_entry
    disk_count_entry = tk.Entry(root, width=10)
    disk_count_entry.pack(pady=5)

    # 계산 버튼
    calculate_button = tk.Button(root, text="편차율 계산", command=calculate_deviation)
    calculate_button.pack(pady=20)

    # 메인 루프 실행
    root.mainloop()

if __name__ == "__main__":
    create_app()
 #pyinstaller --onefile --windowed disk_usage_deviation.py
 #pyinstaller disk_usage_deviation.spec