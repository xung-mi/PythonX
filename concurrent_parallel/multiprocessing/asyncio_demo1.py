import asyncio
import time

# Định nghĩa coroutine để mô phỏng ngủ bất đồng bộ
async def async_sleep(seconds):
    """
    Mô phỏng ngủ trong 'seconds' giây bằng asyncio.sleep.
    In thông báo trước và sau khi ngủ.
    """
    print(f"Trước khi ngủ {seconds} giây")
    await asyncio.sleep(seconds)  # Tạm dừng, nhường quyền cho event loop
    print(f"Sau khi ngủ {seconds} giây")

# Định nghĩa coroutine để trả về giá trị
async def return_hello():
    """
    Trả về chuỗi 'Hello' sau khi đợi 1 giây.
    """
    await asyncio.sleep(1)  # Đợi 1 giây để mô phỏng tác vụ
    return "Hello"

# Định nghĩa coroutine chính
async def main():
    """
    Coroutine chính, chạy các coroutine khác và xử lý kết quả.
    """
    # Chạy async_sleep và đợi hoàn thành
    await async_sleep(5)

    # Chạy return_hello và lấy giá trị trả về
    result = await return_hello()
    print(f"Kết quả từ return_hello: {result}")

# Điểm vào chương trình
if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())  # Khởi động event loop và chạy main
    print(f"Thời gian thực thi: {time.time() - start_time:.2f} giây")