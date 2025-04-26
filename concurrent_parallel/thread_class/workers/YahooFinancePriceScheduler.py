import threading
import time
import random
from workers.YahooFinancePriceWorkers import YahooFinancePriceWorker


class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super().__init__(**kwargs)
        self._input_queue = input_queue
        self.start()

    def run(self):
        while True:
            value = (
                self._input_queue.get()
            )  # Đọc từ Queue (chặn nếu Queue rỗng), tức là đợi đến khi có dữ liệu
            if value == "done":
                break
            worker = YahooFinancePriceWorker(symbol=value)
            price = worker.price
            print(f"Price for {value}: {price}")
            time.sleep(random.random())  # Độ trễ ngẫu nhiên 0-1 giây
