import random

# a. Tạo mảng 4x4 ngẫu nhiên
n = 4
matrix = [[random.randint(-100, 100) for _ in range(n)] for _ in range(n)]

print("Ma trận ban đầu:")
for row in matrix:
    print(row)

# b. Sắp xếp
# Bước 1: dồn tất cả phần tử vào list
flat_list = []
for row in matrix:
    flat_list.extend(row)

# Bước 2: sắp xếp tăng dần
flat_list.sort()

# Bước 3: gán lại vào ma trận
sorted_matrix = []
index = 0
for i in range(n):
    row = []
    for j in range(n):
        row.append(flat_list[index])
        index += 1
    sorted_matrix.append(row)

print("\nMa trận sau khi sắp xếp:")
for row in sorted_matrix:
    print(row)
