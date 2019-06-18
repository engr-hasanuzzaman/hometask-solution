import factory
from utility import get_dict, is_dictionariable, Queue, is_dictionary, leveling 

def print_depth(data):
  for d in calculate_depth(data):
    print("{} {}".format(d[0], d[1]))
# Write function body

# use breath first search algorithm
def calculate_depth(data):
  if not is_dictionariable(data):
    return []

  data = get_dict(data)
  # leveling first level keys
  result = leveling(data.keys(), 1)

  queue = Queue()
  q_elmens = data.values()
  # enqueue all the value with level 2
  for elm in q_elmens:
    queue.enqueue((elm, 2))

  while not queue.is_empty():
    elm, level = queue.dequeue()
    if is_dictionariable(elm):
      elm = get_dict(elm)
      result = result + leveling(elm.keys(), level)
      
      for val in elm.values():
        queue.enqueue((val, level + 1))
  return result

#
# calling print_depth if this file is main file 
#
if __name__ == '__main__':
  print_depth(factory.dict_with_3rd_lev_object)

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

def test_with_10th_level_dict():
  assert calculate_depth(factory.tenth_level_dict) == [
    ["key1", 1], 
    ["key2", 2], 
    ["key3", 3], 
    ["key4", 4], 
    ["key5", 5], 
    ["key6", 6], 
    ["key7", 7], 
    ["key8", 8], 
    ["key9", 9], 
    ["key10", 10]
  ]

def test_dict_with_object():
  assert calculate_depth(factory.dict_with_2nd_lev_object) == [
    ["key1", 1],
    ["key2", 1],
    ["key3", 2],
    ["key4", 2],
    ["key5", 3],
    ["user", 3],
    ["first_name", 4],
    ["last_name", 4],
    ["father", 4],
    ["first_name", 5],
    ["last_name", 5],
    ["father", 5]
  ]

def test_dict_with_3rd_level_object():
  assert calculate_depth(factory.dict_with_3rd_lev_object) == [
    ["key1", 1],
    ["key2", 1],
    ["key3", 2],
    ["key4", 2],
    ["key5", 3],
    ["user", 3],
    ["first_name", 4],
    ["last_name", 4],
    ["father", 4],
    ["first_name", 5],
    ["last_name", 5],
    ["father", 5],
    ["first_name", 6],
    ["last_name", 6],
    ["father", 6]
  ]
