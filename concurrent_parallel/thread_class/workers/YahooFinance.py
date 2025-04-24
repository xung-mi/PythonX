import threading
import requests
import lxml.html
import time
import random


class YahooFinancePriceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super().__init__(**kwargs)  # Khởi tạo lớp cha threading.Thread
        self.symbol = symbol
        self.base_url = "https://finance.yahoo.com/quote/"
        self.url = f"{self.base_url}{symbol}"
        self.start()
        print(f"Starting {self.symbol} with thread {self.name}")

    def run(self):
        time.sleep(random.random() * 30)  # Độ trễ ngẫu nhiên 0-30 giây
        response = requests.get(self.url)
        if response.status_code != 200:
            print(f"Failed to fetch {self.url}")
            return
        page_contents = lxml.html.fromstring(response.text)
        price = page_contents.xpath(
            '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]'
        )[0].text
        print(f"Price for {self.symbol}: {price}")
