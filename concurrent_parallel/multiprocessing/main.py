from multiprocessing import Process, Queue
import time

# Hàm kiểm tra số giá trị trong danh sách trong một phạm vi
def check_values_in_list(i, num_processes, queue, comparison_list):
    # Tính toán giới hạn dưới và trên cho mỗi tiến trình
    max_number = 10_000_000  # Tổng số giá trị cần kiểm tra (10 triệu để đơn giản)
    lower = i * max_number // num_processes  # Giới hạn dưới
    upper = (i + 1) * max_number // num_processes  # Giới hạn trên

    # Đếm số giá trị trong danh sách
    number_of_hits = 0
    for value in range(lower, upper):
        if value in comparison_list:  # Kiểm tra giá trị có trong danh sách
            number_of_hits += 1

    # Đưa kết quả vào Queue (gồm khoảng và số lần tìm thấy)
    queue.put((lower, upper, number_of_hits))

def main():
    start_time = time.time()  # Ghi lại thời gian bắt đầu

    # Danh sách để kiểm tra
    comparison_list = [1, 2, 3]

    # Số lượng tiến trình
    num_processes = 4

    # Tạo Queue để lưu kết quả từ các tiến trình
    queue = Queue()

    # Tạo danh sách các tiến trình
    processes = []
    for i in range(num_processes):
        # Tạo tiến trình với tham số: chỉ số i, tổng số tiến trình, Queue, danh sách
        p.start()  # Bắt đầu tiến trình

    # Chờ tất cả tiến trình hoàn thành
    for p in processes:
        p.join()

    # Lấy và in kết quả từ Queue
    for _ in range(num_processes):
        lower, upper, hits = queue.get()  # Lấy kết quả từ Queue
        print(f"Trong khoảng {lower} đến {upper}: Có {hits} giá trị trong danh sách")

    # Tính và in thời gian thực thi
    print(f"Thời gian thực thi: {time.time() - start_time:.2f} giây")

if __name__ == "__main__":
    main()