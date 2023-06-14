class BST:

    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None

    def insert(self,data):
        if self.data is None:
            self.data = data
            return
        elif self.data > data:
            if self.lchild is None:
                self.lchild = BST(data)
            else:
                self.lchild.insert(data)
        else:
            if self.rchild is None:
                self.rchild = BST(data)
            else:
                self.rchild.insert(data)


    def traversal(self):
        if self.lchild:
            self.lchild.traversal()
        print(self.data)
        if self.rchild:
            self.rchild.traversal()

