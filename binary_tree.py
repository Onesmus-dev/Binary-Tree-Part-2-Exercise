class BinarySearchTreeNode:
    '''
    This code is aimed at using max_val as given Binary Tree Part 2 Exercise
    Max_val = self.right.find_min()
          --->  self.data = max_val
          --->  self.right = self.right.delete(max_val)
    '''
    # Instantiates our binary class
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # Add the val in the left subtree
            if self.left:
                # So now this adds a child to the left node by recursively calling the add_child function
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # Add to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    # In-order Traversal
    def in_order_traversal(self):
        elements = []
        # Visit left
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        # Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # Recursively find the maximum value
    def find_max_recursive(self):
        if not self.right:  # Checks if there is a child to the right
            return self.data  # If not, returns the value
        else:
            return self.right.find_max_recursive()

    # Find the minimum value
    def find_min(self):
        current = self  # This acts as a pointer
        while current.left:  # Loop through the left nodes
            current = current.left  # Update the value of current
        return current.data  # Return the final lowest left value

    # Delete function
    def delete(self, val):
        if val < self.data:  # Checks if the val is on the left side of the tree
            if self.left:
                self.left = self.left.delete(val)  # Recursively calls the delete function till the val = data
            else:
                return None  # If there are no left nodes of the tree
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
            else:
                return None  # You can ignore this else return since in Python it would return None
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # Use min_val from the right subtree to replace the current node
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 23, 18, 34, 56, 3, 10]
    numbers_tree = build_tree(numbers)
    print("In-order traversal:", numbers_tree.in_order_traversal())
    numbers_tree.delete(10)
    print("After deleting 10:", numbers_tree.in_order_traversal())

