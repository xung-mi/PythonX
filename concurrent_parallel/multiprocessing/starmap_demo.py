from multiprocessing import Pool, cpu_count
import time

# Hàm tính lũy thừa
def power(x, y):
    """
    Tính x mũ y.
    x: Số cơ số.
    y: Số mũ.
    Trả về: x^y.
    """
    return x ** y

def main():
    start_time = time.time()  # Ghi lại thời gian bắt đầu

    # Danh sách số và danh sách lũy thừa
    numbers = [1, 2, 3]
    powers = [4, 5, 6]

    # Ghép hai danh sách thành danh sách tuple [(1, 4), (2, 5), (3, 6)]
    input_list = list(zip(numbers, powers))
    print(f"Danh sách đầu vào: {input_list}")

    # Số tiến trình dựa trên số lõi CPU
    num_processes = max(1, cpu_count() - 1)  # Dùng cpu_count() - 1, tối thiểu 1
    print(f"Số tiến trình sử dụng: {num_processes}")

    # Khởi tạo Pool và dùng starmap
    with Pool(processes=num_processes) as pool:
        # Dùng starmap để áp dụng hàm power lên từng tuple trong input_list
        results = pool.starmap(power, input_list)

    # In kết quả
    print(f"Kết quả: {results}")  # [1, 32, 729]

    # In thời gian thực thi
    print(f"Thời gian thực thi: {time.time() - start_time:.2f} giây")

if __name__ == "__main__":
    main()