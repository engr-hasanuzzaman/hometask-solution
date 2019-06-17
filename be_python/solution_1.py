import factory_1  as factory

def print_depth(data):
  print("calling print depth")
  for d in calculateDepth(data):
    print("{} {}".format(d[0], d[1]))
# Write function body

def is_dictionary(d):
  return type(d) is dict

def calculateDepth(data):
  if not is_dictionary(data):
    return []

  # leveling first level keys
  result = leveling(data.keys(), 1)

  queue = Queue()
  return result

def leveling(keys, level):
  return [[key, level] for key in keys]

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

    def is_empty(self):
      return len(self.queue) == 0

if __name__ == '__main__':
  print_depth(factory.second_level_dict)

#
# testing section
#

def test_single_level_traversing():
  assert calculateDepth(factory.single_level_dict) == [["name", 1], ["age", 1], ["passion", 1]]

def test_non_dict_data():
  assert calculateDepth(123) == []

def test_empty_data():
  assert calculateDepth(None) == []