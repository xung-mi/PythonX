import time

from workers.WikiWorkers import WikiWorker
from workers.YahooFinance import YahooFinancePriceWorker

def main():
    calc_time = time.time()
    wiki_worker = WikiWorker()
    current_workers = []
    for symbol in wiki_worker.get_sp_500_companies():
        yahoo_worker = YahooFinancePriceWorker(symbol)
        current_workers.append(yahoo_worker)
        
    for worker in current_workers:
        worker.join()
    print(f"Time taken: {round(time.time() - calc_time, 1)} seconds")

if __name__ == "__main__":
    main()
