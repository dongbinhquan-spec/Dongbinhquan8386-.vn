class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Thêm node vào BST
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Tìm đường đi từ root đến node k
def find_path(root, k, path):
    if root is None:
        return False
    
    path.append(root.val)
    
    if root.val == k:
        return True
    
    if (k < root.val and find_path(root.left, k, path)) or \
       (k > root.val and find_path(root.right, k, path)):
        return True
    
    path.pop()
    return False

# Tìm đường đi từ x đến y
def path_between(root, x, y):
    path_x = []
    path_y = []
    
    find_path(root, x, path_x)
    find_path(root, y, path_y)
    
    # Tìm LCA
    i = 0
    while i < len(path_x) and i < len(path_y) and path_x[i] == path_y[i]:
        i += 1
    
    # Đường từ x -> LCA (đảo ngược)
    path_from_x = path_x[i-1::-1]
    
    # Đường từ LCA -> y
    path_to_y = path_y[i:]
    
    return path_from_x + path_to_y

# ================= MAIN =================
# Nhập dữ liệu
arr = list(map(int, input("Nhập dãy số: ").split()))

root = None
for x in arr:
    root = insert(root, x)

while True:
    try:
        x, y = map(int, input("Nhập x, y: ").split())
        result = path_between(root, x, y)
        print("Đường đi:", *result)
    except:
        break
