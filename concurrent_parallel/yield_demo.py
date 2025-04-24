import requests
from bs4 import BeautifulSoup


def extract_company_symbols(page_html):
    print("Bắt đầu phân tích HTML", flush=True)
    soup = BeautifulSoup(page_html)
    table = soup.find("table", {"id": "constituents"})
    if table:
        for row in table.find_all("tr")[1:]:
            columns = row.find_all("td")
            if columns:
                print(f"Đang trích xuất mã: {columns[0].text.strip()}")
                yield columns[0].text.strip()


# Test
html = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies").text
gen = extract_company_symbols(html)
print("Lấy 3 mã đầu tiên:", flush=True)
for i in range(3):
    print(next(gen), flush=True)
