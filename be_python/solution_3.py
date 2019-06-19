import factory_lca as factory
from utility import get_dict, is_dictionariable, Queue, is_dictionary, leveling 

# Lowest/Least Common Ancestor in a Binary Tree
def lca(node1, node2):
  return None

#
# testing section
#

def test_with_n6_and_n7():
  assert lca(factory.n6, factory.n7) == 3

def test_with_n3_and_n7():
  assert lca(factory.n3, factory.n7) == 3

def test_with_n4_and_n5():
  assert lca(factory.n4, factory.n5) == 2  

def test_with_n4_and_n6():
  assert lca(factory.n4, factory.n6) == 1

def test_with_n3_and_n4():
  assert lca(factory.n3, factory.n4) == 1

def test_with_n2_and_n4():
  assert lca(factory.n2, factory.n4) == 2

def test_with_n15_and_n16():
  assert lca(factory.n15, factory.n16) == 1

def test_with_n19_and_n11():
  assert lca(factory.n19, factory.n11) == 2