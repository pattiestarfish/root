heaps are commonly used in conjunction with priority queues-- ex given using root @ minimum value; child>parent
(can also implement using root as  max value)
heap = tree with 2 qualities: root is min value of dataset, and every child>parent
heaps act in BTs in that each node has <= 2 children, added from left to right
left child = (index * 2) + 1
right child = (index * 2) + 2
parent node = (index - 1) /2 ---> cannot perform on root or will get error

remove an element by heapifying down = cannot easily remove top node, so instead
swap root node(top node) with most bottom right node/leaf, and swap node with the lesser of the 2 children (left vs right)

min heap useful for sorting a dataset or finding the shortest path