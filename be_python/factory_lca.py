#==============================================================
# contains objects used for testing LCA(Least Common Ancestor)
# =============================================================

class Node(object):
  def __init__(self, value, parent=None):
    self.value = value
    self.paren = parent

n1 = Node(1)  
n2 = Node(2, n1)
n3 = Node(3, n1)
n4 = Node(4, n2)
n5 = Node(5, n2)
n6 = Node(6, n3)
n7 = Node(7, n3)
n8 = Node(8, n4)
n9 = Node(9, n4)
n10 = Node(10, n5)
n11 = Node(11, n5)
n12 = Node(12, n6)
n13 = Node(13, n6)
n14 = Node(14, n7)
n15 = Node(15, n7)
n16 = Node(16, n8)
n17 = Node(17, n8)
n18 = Node(18, n9)
n19 = Node(19, n9)
n20 = Node(20, n10)

# above tree is look like the below
#
#                          1
#                         / \
#                        /   \
#                       /     \
#                      /       \
#                     /         \
#                    /           \
#                   /             \
#                  /               \
#                 /                 \
#                2                   3
#               / \                 / \
#              /   \               /   \
#             /     \             /     \
#            /       \           /       \
#           /         \         6         7
#          /           \       / \       / \
#         4             5     /   \     /   \
#        / \           / \   12   13   14   15
#       /   \         /   \
#      /     \       10   11
#     /       \     /
#    8         9   20
#   / \       / \
#  /   \     /   \
# 16   17   18   19
#