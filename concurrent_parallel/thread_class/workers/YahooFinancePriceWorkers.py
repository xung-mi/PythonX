import threading
import requests
import lxml.html
import time


class YahooFinancePriceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super().__init__(**kwargs)
        self.symbol = symbol
        self.base_url = "https://finance.yahoo.com/quote/"
        self.url = f"{self.base_url}{symbol}"
        # Cập nhật headers để tránh bị chặn
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.price = None
        self.start()

    def run(self):
        try:
            # Sử dụng session để duy trì cookies
            response = self.session.get(self.url)

            # Xử lý rate limiting
            if response.status_code == 429:
                time.sleep(2)  # Đợi 2 giây trước khi thử lại
                response = self.session.get(self.url)

            if response.status_code != 200:
                return None

            page_contents = lxml.html.fromstring(response.text)

            # Thử xpath mới để lấy giá
            price_elements = page_contents.xpath(
                '//fin-streamer[@data-field="regularMarketPrice"]'
            )
            if price_elements:
                return price_elements[0].text

            # Backup xpath nếu cái trên không hoạt động
            price_elements = page_contents.xpath(
                '//*[@id="quote-header-info"]//fin-streamer[@data-field="regularMarketPrice"]'
            )
            if price_elements:
                self.price = price_elements[0].text

        except Exception as e:
            return None

        finally:
            self.session.close()


if __name__ == "__main__":
    worker = YahooFinancePriceWorker(symbol="MMM")
    price = worker.run()
    if price:
        print(f"Giá của MMM: {price}")
    else:
        print("Không thể lấy được giá")
