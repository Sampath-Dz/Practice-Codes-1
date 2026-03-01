import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                print("Creating object...")
                cls._instance = super().__new__(cls)
        return cls._instance


def task():
    obj = Singleton()
    print(obj)


threads = []

for i in range(3):
    t = threading.Thread(target=task)
    threads.append(t)


for t in threads:
    t.start()


for t in threads:
    t.join()
