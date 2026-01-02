class TreeNode:

    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        left_key = self.left.key if self.left else None
        right_key = self.right.key if self.right else None
        parent_key = self.parent.key if self.parent else None
        return f"key: {self.key}, value: {self.value}, left: {left_key}, right: {right_key}, parent: {parent_key}"

    def is_balanced(self):

        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        left_height = height(self.left)
        right_height = height(self.right)

        if abs(left_height - right_height) > 1:
            return False

        left_balanced = True
        right_balanced = True
        if self.left:
            left_balanced = self.left.is_balanced()
        if self.right:
            right_balanced = self.right.is_balanced()

        return left_balanced and right_balanced

    # -------- is_valid_bst --------
    def is_bst(self, min_key=None, max_key=None):
        if min_key is not None and self.key <= min_key:
            return False
        if max_key is not None and self.key >= max_key:
            return False

        if self.left:
            if not self.left.is_bst(min_key, self.key):
                return False
        if self.right:
            if not self.right.is_bst(self.key, max_key):
                return False

        return True


    def inorder_iterative(self):
        result = []
        stack = []
        current = self

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append((current.key, current.value))
            current = current.right

        return result

    def print_paths(self):
        self._print_paths_recursive([])

    def _print_paths_recursive(self, path):
        path.append(self.key)

        if self.left is None and self.right is None:
            print(" -> ".join(map(str, path)))
        else:
            if self.left:
                self.left._print_paths_recursive(path)
            if self.right:
                self.right._print_paths_recursive(path)

        path.pop()


def rotate_left(node):
    rotation_root = node
    new_root = rotation_root.right
    if not new_root:
        return

    if new_root.left:
        rotation_root.right = new_root.left
        new_root.left.parent = rotation_root
    else:
        rotation_root.right = None

    new_root.left = rotation_root

    new_root.parent = rotation_root.parent
    if rotation_root.parent:
        if rotation_root.parent.left == rotation_root:
            rotation_root.parent.left = new_root
        else:
            rotation_root.parent.right = new_root

    rotation_root.parent = new_root


def print_tree(node, level=0):
    if not node:
        return
    indent = " " * (4 * level)
    print(f"{indent}{node}")
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)


root = TreeNode(10, '10_val')
node20 = TreeNode(20, '20_val', root)
root.right = node20
node30 = TreeNode(30, '30_val', node20)
node20.right = node30

print("\nIs the tree balanced (Initially)?")
print(root.is_balanced(), end="\n\n")

print("Is the tree a valid BST (Initially)?")
print(root.is_bst(), end="\n\n")

print("before rotation:")
print_tree(root)

rotate_left(root)

new_root = node20
while new_root.parent:
    new_root = new_root.parent

print("\nafter rotation:")
print_tree(new_root)

print("\nIs the tree balanced (after rotation)?")
print(new_root.is_balanced())

print("\nIs the tree a valid BST (after rotation)?")
print(new_root.is_bst())

print("\nIterative inorder traversal from new_root:")
print(new_root.inorder_iterative())

print("\nAll root-to-leaf paths:")
new_root.print_paths()