"""
@Author : Sahil Mulani
@Date : 25-Aug-2024
@Description : To implement and design binaryTree
"""

class emptyTreeException(Exception):
    pass


class bst_Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class bst:

    @staticmethod
    def _inorder(run:bst_Node) -> None:
        if run is not None:
            bst._inorder(run.left)
            print(f"[{run.data}]->",end="")
            bst._inorder(run.right)

    @staticmethod
    def _postOrder(run:bst_Node) -> None:
        if run is not None:
            bst._postOrder(run.left)
            bst._postOrder(run.right)
            print(f"[{run.data}]->",end="")

    @staticmethod
    def _preOrder(run:bst_Node) -> None:
        if run is not None:
            print(f"[{run.data}]->",end="")
            bst._preOrder(run.left)
            bst._preOrder(run.right)

    def __init__(self):
        self.root_node = None
        self.nr_element = 0

    def insert(self, data) -> None:
        """
        @self : calling BST class object
        In this method insert elements one by one in BST
        :param data: data to be inserted
        :return: None
        """
        if data is None:
           print("Value can not be None")

        node = bst_Node(data)
        if self.root_node is None:
            self.root_node = node
            self.nr_element += 1
        else:
            run = self.root_node
            while True:
                if run.data < data:
                    if run.right is None:
                        run.right = node
                        run.right.parent = run
                        self.nr_element += 1
                        break
                    else:
                        run = run.right
                else:
                    if run.left is None:
                        run.left = node
                        run.left.parent = run
                        self.nr_element += 1
                        break
                    else:
                        run = run.left

    def min(self) -> any:
        """
        @self calling BST object
        Return a min data value help by any node in BST @self
        Raise bst_empty exception if the tree is empty
        :return:
        """
        if self.root_node is None:
            raise emptyTreeException("Cannot find min in empty tree")
        run = self.root_node
        while run.left is not None:
            run = run.left

        return run.data

    def searchNode(self, root_node : bst_Node, data):
        run = root_node

        while run is not None:

            if data == run.data:
                break
            elif data > run.data:
                run = run.right
            elif data < run.data:
                run = run.left

        return run

    def max(self) -> any:
        """
        @self : calling BST object
        Return Max value from BST tree
        :return: If BST Tree is empty return empty tree exception
        """

        if self.root_node is None:
            raise emptyTreeException("cannot perform Max operation on empty tree")

        run = self.root_node
        while run.right is not None:
            run = run.right

        return run.data

    def search(self, s_data: any):
        """
        @self : calling BST node object
        In this method will search the element is present or not
        :param s_data: Value to be search
        :return: True is s_data is present otherwise false
        """
        run = self.root_node
        while run is not None:
            if s_data == run.data:
                return True
            if s_data < run.data:
                run = run.left
            if s_data > run.data:
                run = run.right

        return False

    def removeNode(self, data) -> None:
        """
        @self : calling BST node object
        In this method will search and remove node from BST
        :param data: Node data to be delete
        :return: None
        """
        z = self.searchNode(self.root_node, data)
        if z is None:
            print("Removed element not found")

        if z.left is None:

            if z.parent is None:
                self.root_node = z.right
            if z.parent.left == z:
                z.parent.left = z.right
            else:
                z.parent.right = z.right
            if z.right is not None:
                z.right.parent = z.parent
        elif z.right is None:

            if z.parent is None:
                self.root_node = z.right
            if z.parent.left == z:
                z.parent.left = z.left
            else:
                z.parent.right = z.left
            if z.left is not None:
                z.left.parent = z.parent

        elif z.left is not None and z.right is not None:
            y =  z.right
            while y.left is not None:
                y = y.left

            if y != z.right:
                y.parent.left = y.right
                if y.right is not None:
                    y.right.parent = y.parent

                y.right = z.right
                y.right.parent = y

            y.left = z.left
            y.left.parent = y

            if z.parent is None:
                self.root_node = y
            elif z is z.parent.left:
                z.parent.left = y
            else:
                z.parent.right = y

            y.parent = z.parent


    def inorder(self) -> None:
        """
        @self : calling BST object
        Travel through a BST @self using inorder sequence
        :return: None
        """
        print("[Start]->", end="")
        self._inorder(self.root_node)
        print("[End]")

    def postOrder(self) -> None:
        """
        @self : calling BST object
        Travel through a BST @self using preorder sequence
        :return: None
        """
        print("[Start]->", end="")
        self._postOrder(self.root_node)
        print("[End]->")

    def preOrder(self) -> None:
        """
        @self : calling BST object
        Travel through a BST @self using preorder sequence
        :return: None
        """
        print("[Start]->", end="")
        self._preOrder(self.root_node)
        print("[End]")

def main():
    L = [10,69,200,42,66,
         57,39,20,200,80,
         444,4.7,89,700]

    T = bst()

    for elm in L:
        T.insert(elm)

    print("Total Number Of Elements Inserted :- ", T.nr_element)
    print("Minimum Element From Tree :- ", T.min())
    print("Maximum Element From Tree :- ", T.max())
    print("Check Valid 89 Is Present Tn The Tree :- ", T.search(89))
    print("Check Invalid 10001 Is Present In The Tree :- ", T.search(10001))
    print("Inorder Traversal :- ", end="")
    T.inorder()
    print("Postorder Traversal :- ", end="")
    T.postOrder()
    print("Preorder4 Traversal :- ", end="")
    T.preOrder()

    print("Remove 39 element")
    T.removeNode(39)
    print("Inorder Traversal :- ", end="")
    T.inorder()
    print("Postorder Traversal :- ", end="")
    T.postOrder()
    print("Preorder4 Traversal :- ", end="")
    T.preOrder()
main()


