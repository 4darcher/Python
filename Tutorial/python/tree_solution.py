class PerfectBST:

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = PerfectBST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = PerfectBST.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = PerfectBST.Node(data)
            else:
                self._insert(data, node.right)

    def __iter__(self):
        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._get_height(node.left), self._get_height(node.right))


def create_bst(sorted_list):
    bst = PerfectBST()
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst


def _insert_middle(sorted_list, first, last, bst):
    if len(sorted_list) == 0:
        return None
    elif len(sorted_list) == 1:
        bst.insert(sorted_list[0])
    else:
        mid = first + last // 2
        bst.insert(sorted_list[mid])
        if last - first == 1:
            bst.insert(last[1])
            bst.insert(first[0])
        if last == first:
            bst.insert(first[0])
        left_first = first
        left_last = mid - 1
        if left_last > left_first:
            bst.insert(left_first)
            bst.insert(left_last)
        right_first = mid + 1
        right_last = last
        if right_first > right_last:
            bst.insert(right_last)
            bst.insert(right_first)
    return sorted_list


balancedTree1 = create_bst(
    [1, 2, 3, 4, 5, 6, 7])
singleTree = create_bst([42])
emptyTree = create_bst([])
print(balancedTree1.get_height())  # 3
print(singleTree.get_height())  # 1
print(emptyTree.get_height())  # 0
