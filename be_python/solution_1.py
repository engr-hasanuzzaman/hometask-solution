import factory_1  as factory

def print_depth(data):
  for d in calculate_depth(data):
    print("{} {}".format(d[0], d[1]))
# Write function body

def is_dictionary(d):
  return type(d) is dict

# use breath first search algorithm
def calculate_depth(data):
  if not is_dictionary(data):
    return []

  # leveling first level keys
  result = leveling(data.keys(), 1)

  queue = Queue()
  q_elmens = data.values()
  # enqueue all the value with level 2
  for elm in q_elmens:
    queue.enqueue((elm, 2))

  while not queue.is_empty():
    elm, level = queue.dequeue()
    if is_dictionary(elm):
      result = result + leveling(elm.keys(), level)
      
      for val in elm.values():
        queue.enqueue((val, level + 1))
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

#
# calling print_depth if this file is main file 
#
if __name__ == '__main__':
  print_depth(factory.original_dict)

#
# testing section
#

def test_single_level_traversing():
  assert calculate_depth(factory.single_level_dict) == [["name", 1], ["age", 1], ["passion", 1]]

def test_non_dict_data():
  assert calculate_depth(123) == []

def test_empty_data():
  assert calculate_depth(None) == []

def test_3rd_level_traversing():
  assert calculate_depth(factory.third_level_dict) == [["name", 1], ["age", 1], ["passion", 1], ["address", 1], ["parents", 1], ["district", 2], ["country", 2], ["father", 2], ["mother", 2], ["fName", 3], ["fAge", 3], ["mName", 3], ["mAge", 3], ["mProfession", 3]]

def test_with_sample_input():
  assert calculate_depth(factory.original_dict) == [["key1", 1], ["key2", 1], ["key3", 2], ["key4", 2], ["key5", 3]]
