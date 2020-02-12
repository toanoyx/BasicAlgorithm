
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def preOrder(root, res=[]):
    if root:
        res.append(root.val)
        preOrder(root.left, res)
        preOrder(root.right, res)
    return res


def inOrder(root, res=[]):
    if root:
        inOrder(root.left, res)
        res.append(root.val)
        inOrder(root.right, res)
    return res


def postOrder(root, res=[]):
    if root:
        postOrder(root.left, res)
        postOrder(root.right, res)
        res.append(root.val)
    return res


def BFS(root):
    res = []
    queue = [root]
    while queue:
        currentNode = queue.pop(0)
        res.append(currentNode.val)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    return res


def DFS(root):
    res = []
    stack = [root]
    while stack:
        currentNode = stack.pop()
        res.append(currentNode.val)
        if currentNode.right:
            stack.append(currentNode.right)
        if currentNode.left:
            stack.append(currentNode.left)
    return res


if __name__ == "__main__":
    tree = TreeNode("1")
    n2 = TreeNode("2")
    n3 = TreeNode("3")
    n4 = TreeNode("4")
    n5 = TreeNode("5")
    n6 = TreeNode("6")
    n7 = TreeNode("7")
    n8 = TreeNode("8")
    n9 = TreeNode("9")

    tree.left, tree.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    n4.left, n4.right = n8, n9

    print("preOrder:" + str(list(preOrder(tree))))
    print("inOrder:" + str(list(inOrder(tree))))
    print("postOrder:" + str(list(postOrder(tree))))
    print("BFS:" + str(list(BFS(tree))))
    print("DFS:" + str(list(DFS(tree))))
