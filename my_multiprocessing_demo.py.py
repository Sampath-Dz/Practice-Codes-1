import multiprocessing
import time

def heavy_task(number):
    print(f"Process {number} starting heavy calculation")
    total = 0
    for i in range(1, 10000000):
        total += i
    print(f"Process {number} finished calculation")

# 👇 VERY IMPORTANT BLOCK
if __name__ == "__main__":

    p1 = multiprocessing.Process(target=heavy_task, args=(1,))
    p2 = multiprocessing.Process(target=heavy_task, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All heavy tasks completed!")
