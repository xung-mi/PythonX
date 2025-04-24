import time

from workers import SquaredSumWorker, SleepyWorker

def main():
    numbers = [1, 2, 3, 4, 5]
    squared_sum_worker = SquaredSumWorker(numbers)
    sleepy_worker = SleepyWorker(seconds=2)

    squared_sum_worker.join()
    sleepy_worker.join()

    print("All workers finished")
    print("Main thread finished")


if __name__ == "__main__":
    main()
