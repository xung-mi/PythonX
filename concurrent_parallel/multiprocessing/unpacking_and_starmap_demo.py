from multiprocessing import Pool, cpu_count
import time

# Hàm kiểm tra số giá trị trong danh sách trong một phạm vi
def check_number_of_values_in_range(comparison_list, lower, upper):
    """
    comparison_list: Danh sách cần kiểm tra.
    lower, upper: Giới hạn dưới và trên.
    Trả về: Số lần giá trị trong danh sách xuất hiện trong phạm vi.
    """
    number_of_hits = 0
    for i in range(lower, upper):
        if i in comparison_list:
            number_of_hits += 1
    return number_of_hits

def main():
    start_time = time.time()  # Ghi lại thời gian bắt đầu

    # Danh sách cần kiểm tra
    comparison_list = [1, 2, 3]

    # Tổng phạm vi và số tiến trình
    max_number = 10_000_000  # 10 triệu để đơn giản
    num_processes = max(1, cpu_count() - 1)  # Dùng cpu_count() - 1, tối thiểu 1
    print(f"Số tiến trình sử dụng: {num_processes}")

    # Tạo danh sách các phạm vi
    step = max_number // num_processes  # Kích thước mỗi phạm vi
    bounds = [(i * step, (i + 1) * step) for i in range(num_processes)]  # [(0, 2.5M), (2.5M, 5M), ...]

    # Chuẩn bị danh sách đầu vào cho starmap
    input_list = [[comparison_list, lower, upper] for lower, upper in bounds]
    print(f"Danh sách đầu vào: {input_list}")

    # Khởi tạo Pool và dùng starmap
    with Pool(processes=num_processes) as pool:
        # Dùng starmap với unpacking (*)
        results = pool.starmap(check_number_of_values_in_range, input_list)

    # In kết quả
    for (lower, upper), hits in zip(bounds, results):
        print(f"Trong khoảng {lower} đến {upper}: Có {hits} giá trị trong danh sách")

    # In thời gian thực thi
    print(f"Thời gian thực thi: {time.time() - start_time:.2f} giây")

if __name__ == "__main__":
    main()