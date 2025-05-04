from multiprocessing import Pool, cpu_count
import time

# Hàm đơn giản để tính bình phương một số
def square(number):
    return number * number  # Trả về bình phương của số đầu vào

def main():
    start_time = time.time()  # Ghi lại thời gian bắt đầu

    # Danh sách đầu vào
    input_list = [1, 2, 3, 4, 5]

    # Xác định số tiến trình dựa trên số lõi CPU
    num_processes = max(1, cpu_count() - 1)  # Dùng cpu_count() - 1, tối thiểu 1 tiến trình
    print(f"Số tiến trình sử dụng: {num_processes}")

    # Khởi tạo Pool với số tiến trình
    with Pool(processes=num_processes) as pool:
        # Sử dụng phương thức map để áp dụng hàm square lên input_list
        results = pool.map(square, input_list)

    # In kết quả
    print(f"Kết quả: {results}")  # Danh sách các giá trị đã được bình phương

    # In thời gian thực thi
    print(f"Thời gian thực thi: {time.time() - start_time:.2f} giây")

if __name__ == "__main__":
    main()