#!python
from collections import deque
# use appendleft of deque to append at the front of the double ended queue
# from queue import LinkedQueue

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        return self.left == None and self.right == None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return self.left != None or self.right != None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)."""
        # TODO: Check if left child has a value and if so calculate its height
        if not self.is_leaf():
            right_height = 0
            left_height = 0
            if self.right != None:
                # make a new height variable without changing property of node
                right_height = self.right.height()
            if self.left != None:
                # ask for the right node height
                left_height = self.left.height()
            # Return one more than the greater of the left height and right height
            # if left_height doesn't exsit, gonna return error, so we assign 0 to l_h, r_h on top
            # max(0, None) is None, all empty list, tuple is false
            return 1 + max(right_height, left_height)
        # if node doesn't have child, height is 0
        return 0

# might have empty seat in hashtable, but in tree all node have data, so tree has the advantage of memory storage
# in unbalanced tree, you need to pay more run time cost
class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        """
        # TODO: Check if root node has a value and if so calculate its height
        if self.root:
            # recursively call the height function
           return self.height()
        raise ValueError("tree empty nooooo")

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
         TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # TODO: Return the node's data if found, or None
        if node is not None:
            return node.data
        else:
            return None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # TODO: Create a new root node
            self.root = BinaryTreeNode(item)
            # TODO: Increase the tree size
            self.size += 1
            # exsit out of the function after we insert root item ! so we call retrun
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item)
        # tree has no duplicate
        # if item == parent.data:
        #     raise ValueError("item already in tree")
        # TODO: Check if the given item should be inserted left of parent node
        if item < parent.data:
            # TODO: Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        # TODO: Check if the given item should be inserted right of parent node
        elif item > parent.data:
            # TODO: Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        # TODO: Increase the tree size
        self.size += 1


    def delete(self, item):
        """ delete the given item in this binary search tree."""
        # (find predicessor 9the node that's immediately next to order of root node)
        if self.is_empty():
            raise ValueError("your tree is empty")
        else:
            # find parent node of the should be deleted item
            parent = self._find_parent_node(item)
            # if item smaller than parent, it's on the left
            if item < parent.data:
                # reset left to None
                parent.left = None
            elif item > parent.data:
                parent.right = None
            self.size -= 1

# ( private function ) underscore show that it's a helper method
    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if node.data == item:
                return node
            # TODO: Check if the given item is less than the node's data
            elif node.data > item:
                # TODO: Descend to the node's left child
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif node.data < item:
                # TODO: Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    # This space intentionally left blank (please do not delete this comment)

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse left subtree, if it exists
        if node.left:
            self._traverse_in_order_recursive(node.left, visit)
        # TODO: Visit this node's data with given function
        visit(node.data)
        # TODO: Traverse right subtree, if it exists
        if node.right:
            self._traverse_in_order_recursive(node.right, visit)

# To get all nodes in a hashtable: it's o(nl) run time, n is num of buckets, l is length of linked list . ln is (entry num)
    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)\
        # Start at the given node's root
        node_stack = LinkedQueue()
        node_stack.prepend(node)
        if node.left:
            node_stack.prepend(node.left)
        while node_stack is not None:
            # first check left leaves caz we are using queue, first in first out.
            while node.left:
                # put left node in the front of the queue
                node_stack.appendleft(node.left)
                node = node.left
            # after going through all left leaves , look for right
            else:
                # pop out item from front if no more left
                node = node_stack.popleft()
                visit(node.data)
                # check right to see if it has left
                if node.right:
                    # append at front
                    node_stack.appendleft(node.right)
                    node = node.right
        return


    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Visit this node's data with given function
        if node:
            visit(node.data)
            # TODO: Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.left, visit)
            # TODO: Traverse right subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        node_stack = []
        node_stack.append(self.root)
        while node_stack:
            # pop the top item in the stack
            node = node_stack.pop()
            visit(node.data)
            # append right_child first and then left_child, caz we want to visit left before right
            if node.right:
                node_stack.append(node.right)
            if node.left:
                node_stack.append(node.left)
            if node.left:
                node_stack.append(self.root)
            if node.right:
                node_stack.append(node.right)

# lexicoghraphic, binary search tree is ordered
    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse left subtree, if it exists
        # deepest call stack is height, so it's only O(log2^n) memory management,same running time : o(n)
        # better to use recursive then iterative to traverse
        if node:
            self._traverse_post_order_recursive(node.left, visit)
            # TODO: Traverse right subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit)
            # TODO: Visit this node's data with given function
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        stack_node = []
        visit_node = []
        # root node on bottom caz we visit it last
        stack_node.append(self.root)
        # make left_node on top, right_node on bottom stack
        while len(stack_node) > 0:
            # first node is root that poped from stack node
            # remove root from stack_node
            node = stack_node.pop()
            # append root to visit_node
            if node.right:
                stack_node.append(node.right)
            if node.left:
                stack_node.append(node.left)

        while (len(visit_node) > 0):
            # pop the left node first, then right node
            node = stack_node.pop()
            visit(node.data)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

# !! both running time and memory storage is big O(N)(n is num of node, based on the num of node in the base level)
    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Create queue to store nodes not yet traversed in level-order
        queue = deque()
        # TODO: Enueue given starting node
        queue.append(start_node)
        # TODO: Loop until queue is empty
        while len(queue) > 0:
            # TODO: Dequeue node at front of queue
            # if linked list que, O(1), if regular queue: o(n)
            # enqueue alwyas o(1) for both implementation
            # logrithsm: which power should I raise base to that reaches 2^n: height: log(2^n)
            # double the nodes, and the level/height only inches up
            # facebook has a billion user, which is 2^30, we only need to go 30 levels deep to search through all users
            # if you double your users, it only need to expand one level deep
            # memory management: half billion user on the base level: o(n), n is number of nodes
            node = queue.popleft()
            # TODO: Visit this node's data with given function
            visit(node.data)
            # TODO: Enqueue this node's left child, if it exists
            if node.left:
                queue.append(node.left)
             # TODO: Enqueue this node's right child, if it exists
            if node.right:
                queue.append(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
