import time
import random
import threading


def do_something_else():
    time.sleep(random.random())

# LR and LW are class attributes in the RW class.
# They serve as read and write locks. The integer
# variable read_count in RW tracks the number of readers.
class RW:
    data = 0
    LR = threading.Condition()
    read_count = 0
    LW = threading.Lock()


class Reader(threading.Thread):
    """The Reader class prints data from the RW class while running.
    It manipulates the RW.read_count by incrementing before a read
    and by decrementing after a read."""
    def __init__(self, name):
        super().__init__(name=name, daemon=True)

    def run(self):
        while True:
            with RW.LR:
                RW.read_count += 1df

