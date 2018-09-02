class Circular:
    def __init__(self, size=5):
        self.size = size
        self.count = 0
        self.data = [''] * self.size
        self.length = len(self.data)
        self.head = 0
        self.tail = 0

    def __str__(self):
        data_list = []
        for e, i in enumerate(self.data):
            particle = [str(i), ""]

            if e == self.head and e == self.tail:
                particle[1] = "ht"
            elif e == self.head:
                particle[1] = "h"
            elif e == self.tail:
                particle[1] = "t"
            else:
                particle[1] = ""
            data_list.append(tuple(particle))

        # return "count: {}, data: {}".format(self.count, data_list)
        return "count: {}, data: {}".format(self.count, self.data)


    def enqueue(self, item):
        if self.count == self.length:
            print("queue is full, adding {} more empty cells".format(self.size))
            piece_1 = self.data[self.head:]
            piece_2 = self.data[:self.head]
            self.data = piece_1 + piece_2 + [''] * self.size
            self.head = 0
            self.tail = self.length
            self.length = len(self.data)
        self.data[self.tail] = item
        self.tail = (self.tail + 1) % self.length
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("Cannot dequeue from empty queue")
            return None
        result = self.data[self.head]
        self.data[self.head] = ''
        self.head = (self.head + 1) % self.length
        self.count -= 1
        return result

    def get_size(self):
        return self.count

# Testing
c = Circular(size=5)
print(c)
x = 0
for _ in range(3):
    c.enqueue(x)
    print(x, str(c))
    x += 1
for _ in range(4):
    print(c.dequeue())
    print(x, str(c))
    x += 1
for _ in range(8):
    c.enqueue(x)
    print(x, str(c))
    x += 1
for i in range(10):
    c.dequeue()
    print(x, str(c))
    x += 1
