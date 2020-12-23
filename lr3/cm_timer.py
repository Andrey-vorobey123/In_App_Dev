from time import time, sleep
from datetime import datetime
from contextlib import contextmanager
import time


class cm_timer_1:

    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.time()
        return 333

    def __exit__(self, exp_type, exp_value, traceback):
        print(time.time() - self.start, '\n')

@contextmanager
def cm_timer_2():
    start = datetime.now()
    yield
    print(datetime.now() - start)

if __name__ == '__main__':
    with cm_timer_1():
        sleep(2.5)

    with cm_timer_2():
        sleep(3)
