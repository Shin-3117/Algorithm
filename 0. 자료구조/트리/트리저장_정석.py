arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child):
        if(not self.left):
            self.left = child
            return
        if(not self.right):
            self.right = child
            return
        return

    def preorder(self):
        if self != None:
            print(self.value, end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    # 중위 순회
    def inorder(self):
        if self != None:
            if self.left:
                self.left.inorder()
            print(self.value, end=' ')
            if self.right:
                self.right.inorder()

    # 후위 순회
    def postorder(self):
        if self != None:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.value, end=' ')

# 이진 트리 만들기
nodes = [TreeNode(i) for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].insert(nodes[childNode])

nodes[1].preorder()
print()
nodes[1].inorder()
print()
nodes[1].postorder()

