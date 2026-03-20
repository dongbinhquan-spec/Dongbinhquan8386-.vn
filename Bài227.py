class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Thêm vào BST
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Tìm LCA trong BST
def find_LCA(root, x, y):
    while root:
        if x < root.val and y < root.val:
            root = root.left
        elif x > root.val and y > root.val:
            root = root.right
        else:
            return root.val

# ================= MAIN =================
# Nhập dữ liệu
arr = list(map(int, input("Nhập dãy số: ").split()))

root = None
for v in arr:
    if v == 0:  # kết thúc dãy
        break
    root = insert(root, v)

while True:
    try:
        x, y = map(int, input("Nhập a, b: ").split())
        print("Node cha:", find_LCA(root, x, y))
    except:
        break
