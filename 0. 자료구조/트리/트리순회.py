import sys
sys.stdin = open("./0. 자료구조/트리/트리순회.txt", "r")

class Node():
    def __init__(self,data,left_node,right_node) -> None:
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


n= int(input())
tree = {}
for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None": left_node = None
    if right_node == "None": right_node = None
    tree[data] = Node(data, left_node, right_node)

# 전위 순회 (Preorder Traversal) : 루트를 먼저 방문합니다.
def pre_order(node):
    print(node.data, end=" ")
    if node.left_node != None: pre_order(tree[node.left_node])
    if node.right_node != None: pre_order(tree[node.right_node])

# 중위 순회 (Inorder Traversal) : 왼쪽 자식을 방문한 뒤에 루트를 방문합니다.
def in_order(node):
    if node.left_node != None: in_order(tree[node.left_node])
    print(node.data, end=" ")
    if node.right_node != None: in_order(tree[node.right_node])

# 후위 순회 (post-order Traversal) : 오른쪽 자식을 방문한 뒤에 루트를 방문합니다.
def post_order(node):
    if node.left_node != None: post_order(tree[node.left_node])
    if node.right_node != None: post_order(tree[node.right_node])
    print(node.data, end=" ")

pre_order(tree['A'])# A B D E C F G 
print() 
in_order(tree["A"])# D B E A F C G 
print() 
post_order(tree["A"])# D E B F G C A 