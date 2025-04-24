import requests
from bs4 import BeautifulSoup


class WikiWorker:
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    @staticmethod
    def _extract_companies(page_html):
        soup = BeautifulSoup(page_html)  # , "lxml")
        table = soup.find(id="constituents")
        table_rows = table.find_all("tr")
        for table_row in table_rows[1:]:
            symbol = table_row.find("td").text.strip("\n")
            yield symbol

    def get_sp_500_companies(self):
        response = requests.get(self._url)
        if response.status_code != 200:
            print(f"Failed to fetch {self._url}")
            return []

        print(response.text)
        yield from self._extract_companies(response.text)  # yield


if __name__ == "__main__":
    worker = WikiWorker()
    for symbol in worker.get_sp_500_companies():
        print(symbol)
        
        # //*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span
