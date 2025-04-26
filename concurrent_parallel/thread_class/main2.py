import time

from workers.WikiWorkers import WikiWorker
from multiprocessing import Queue
from workers.YahooFinancePriceScheduler import YahooFinancePriceScheduler


def main():
    start_time = time.time()
    symbol_queue = Queue()  # Tạo Queue để lưu mã chứng khoán

    wiki = WikiWorker()

    num_workers = 4

    scheduler_threads = [
        YahooFinancePriceScheduler(input_queue=symbol_queue)
        for _ in range(
            num_workers
        )  # tương đương với việc tạo 4 yahoo finance price scheduler
    ]

    # Producer: Đưa mã chứng khoán vào Queue
    for symbol in wiki.get_sp_500_companies():
        symbol_queue.put(symbol)

    # Producer: Đưa mã chứng khoán vào Queue
    for symbol in wiki.get_sp_500_companies():
        symbol_queue.put(symbol)

    # Đưa tín hiệu "done" để dừng các scheduler
    for _ in range(num_workers):
        symbol_queue.put("done")

    # Đợi tất cả scheduler hoàn thành
    for scheduler in scheduler_threads:
        scheduler.join()

    print(f"Time taken: {round(time.time() - start_time, 1)} seconds")


if __name__ == "__main__":
    main()
