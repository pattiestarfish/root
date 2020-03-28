root: A node which has no parent. One per tree.
parent: A node which references other nodes.
child: Nodes referenced by other nodes.
sibling: Nodes which have the same parent.
leaf: Nodes which have no children.
level: The height or depth of the tree. Root nodes are at level 1, their children are at level 2, and so on.

# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    print("initializing node...")

seed =  TreeNode('pat')
print(seed.value)

# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
root.add_child(child)
--------------------------------------------------
# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __repr__(self):
    return str(self.children)

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    print(self.children)
    self.children = [child for child in self.children if child != child_node]
    # new_children = []
    # for child in self.children:
    #  if child != child_node:
    #    new_children.append(child)
    # self.children = new_children


root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)

root.remove_child(bad_seed)
print(root)


#_------------------------ traverse function
# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children
                     if child is not child_node]

  def traverse(self):
    print(self.value)
    for child in self.children:
      print(child.value)


root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")

root.add_child(first_child)
root.add_child(second_child)
root.traverse()

#------------------------traversing entire treemy laptop with while loop
# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children
                     if child is not child_node]

  def traverse(self):
    print("Traversing...")
    nodes_to_visit = [self]
    while len(nodes_to_visit) != 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children
    else:
      return


root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)

root.traverse()
