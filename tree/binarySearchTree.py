from queue import Queue
import math


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self, val_list=[]):
        self.root = None
        for n in val_list:
            self.insert(n)

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            node = self.root
            while node:
                p = node
                if data < node.val:
                    node = node.left
                else:
                    node = node.right
            new_node = TreeNode(data)
            new_node.parent = p
            if data < p.val:
                p.left = new_node
            else:
                p.right = new_node
        return True

    def search(self, data):
        res = []
        node = self.root
        while node:
            if data < node.val:
                node = node.left
            else:
                if data == node.val:
                    res.append(node)
                node = node.right
        return res

    def delete(self, data):
        del_list = self.search(data)
        for n in del_list:
            if n.parent is None and n != self.root:
                continue
            else:
                self._del(n)

    def _del(self, node):
        # 1
        if node.left is None and node.right is None:
            if node == self.root:
                self.root = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = None
                else:
                    node.parent.right = None
                node.parent = None
        # 2
        elif node.left is None and node.right is not None:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                node.right = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent
                node.parent = None
                node.right = None
        elif node.left is not None and node.right is None:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                node.left = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
                node.parent = None
                node.left = None
        # 3
        else:
            min_node = node.right
            if min_node.left:
                min_node = min_node.left
            if node.val != min_node.val:
                node.val = min_node.val
                self._del(min_node)
            else:
                self._del(min_node)
                self._del(node)

    def get_min(self):
        if self.root is None:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.val

    def get_max(self):
        if self.root is None:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.val

    def in_order(self):
        if self.root is None:
            return []
        return self._in_order(self.root)

    def _in_order(self, node):
        if node is None:
            return []
        res = []
        n = node
        res.extend(self._in_order(n.left))
        res.append(n.val)
        res.extend(self._in_order(n.right))
        return res

    def __repr__(self):
        print(str(self.in_order()))
        return self._draw_tree()

    def _bfs(self):
        if self.root is None:
            return []
        res = []
        q = Queue()
        q.put((self.root, 1))
        while not q.empty():
            n = q.get()
            if n[0] is not None:
                res.append((n[0].val, n[1]))
                q.put((n[0].left, n[1] * 2))
                q.put((n[0].right, n[1] * 2 + 1))
        return res

    def _draw_tree(self):
        nodes = self._bfs()
        if not nodes:
            print('This tree has no nodes.')
            return
        layer_num = int(math.log(nodes[-1][1], 2)) + 1
        prt_nums = []
        for i in range(layer_num):
            prt_nums.append([None] * 2 ** i)
        for v, p in nodes:
            row = int(math.log(p, 2))
            col = p % 2 ** row
            prt_nums[row][col] = v
        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + '\n'
        return prt_str


if __name__ == '__main__':
    nums = [4, 2, 5, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)
    print(bst)

    # 插入
    bst.insert(1)
    bst.insert(4)
    print(bst)

    # 搜索
    for n in bst.search(2):
        print(n.parent.val, n.val)

    # 删除
    bst.insert(6)
    bst.insert(7)
    print(bst)
    bst.delete(7)
    print(bst)
    bst.delete(6)
    print(bst)
    bst.delete(4)
    print(bst)

    # min max
    print(bst.get_max())
    print(bst.get_min())
