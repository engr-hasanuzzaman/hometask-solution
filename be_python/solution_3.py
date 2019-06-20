from collections import OrderedDict
import factory_lca as factory

# Lowest/Least Common Ancestor in a Binary Tree
def lca(node1, node2):
  node1_ancestors_values = get_ancestors(node1).keys()
  node2_ancestors_dict = get_ancestors(node2)

  for val in node1_ancestors_values:
    if val in node2_ancestors_dict:
      return val

def get_ancestors(node):
  if node is None:
    return {}

  ancestors_dict = OrderedDict()
  while node is not None:
    ancestors_dict[node.value] = None
    node = node.parent

  return ancestors_dict


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

def test_with_n5_and_n10():
  assert lca(factory.n5, factory.n10) == 5

def test_with_n17_and_n18():
  assert lca(factory.n17, factory.n18) == 4