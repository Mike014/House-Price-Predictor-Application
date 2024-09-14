import threading

class Concurrency:
    def __init__(self, target, *args):
        self.thread = threading.Thread(target=target, args=args)

    def start(self):
        self.thread.start()

    def join(self):
        self.thread.join()
