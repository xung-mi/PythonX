import threading

class SquaredSumWorker(threading.Thread):
    def __init__(self, numbers, **kwargs):
        self._numbers = numbers
        super(SquaredSumWorker, self).__init__(**kwargs)
        self.start()

    def _calculate_squared_sum(self):
        return sum(x * 2 for x in self._numbers)
    
    def run(self):
        result = self._calculate_squared_sum()
        print(f"{self.name} - Squared sum: {result}")






        