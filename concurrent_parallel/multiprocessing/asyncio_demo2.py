import asyncio
import time

# Coroutine mô phỏng giấc ngủ với số thứ tự
async def async_sleep(seconds, task_id):
    """
    Mô phỏng ngủ trong 'seconds' giây, in thông báo trước và sau.
    task_id: Số thứ tự để phân biệt task.
    """
    print(f"Task {task_id}: Trước khi ngủ {seconds} giây")
    await asyncio.sleep(seconds)  # Nhường quyền cho event loop
    print(f"Task {task_id}: Sau khi ngủ {seconds} giây")

# Coroutine chính
async def main():
    """
    Tạo và chạy hai tasks đồng thời, in thời gian thực thi.
    """
    start_time = time.time()  # Ghi lại thời gian bắt đầu

    # Tạo task cho coroutine thứ nhất
    task1 = asyncio.create_task(async_sleep(5, 1))  # Lên lịch task 1
    # Tạo task cho coroutine thứ hai
    task2 = asyncio.create_task(async_sleep(5, 2))  # Lên lịch task 2

    # Đợi kết quả của các task
    await task1  # Đợi task 1 hoàn thành
    await task2  # Đợi task 2 hoàn thành

    # In thời gian thực thi
    print(f"Thời gian thực thi: {time.time() - start_time:.2f} giây")

# Chạy chương trình
if __name__ == "__main__":
    asyncio.run(main())  # Khởi động event loop và chạy main