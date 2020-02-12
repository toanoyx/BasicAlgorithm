from typing import TypeVar, Generic, Generator, Optional

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, value: T):
        self.val = value
        self.left = None
        self.right = None


def preOrder(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield root.val
        yield from preOrder(root.left)
        yield from preOrder(root.right)


def inOrder(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from inOrder(root.left)
        yield root.val
        yield from inOrder(root.right)


def postOrder(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from postOrder(root.left)
        yield from postOrder(root.right)
        yield root.val


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

    print("preOrder: " + str(list(preOrder(tree))))
    print("inOrder: " + str(list(inOrder(tree))))
    print("postOrder: " + str(list(postOrder(tree))))