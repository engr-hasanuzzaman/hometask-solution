def print_depth(data):
  return False
# Write function body

def is_dictionary(d):
  return type(d) is dict

def calculateDepth(data):
  result = []
  queue = Queue()
  return result

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)   