
def is_dictionary(d):
  '''Returns True is passing data is dictionary otherwise False '''
  return type(d) is dict

def is_dictionariable(d):
  '''Returns True is passing data is dictionary or python object with __dict__ attribute otherwise False '''
  return is_dictionary(d) or hasattr(d, "__dict__")

# ensure return python dict object
def get_dict(obj):
  if is_dictionary(obj):
    return obj
  else:
    return vars(obj)

def leveling(keys, level):
  '''Assing level to keys and return array or [key, level]'''
  return [[key, level] for key in keys]

# Simplte queue implementation
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