import sys
import random

# Ghi ma trận vào file
def write_matrix(filename, matrix):
    with open(filename, 'w') as f:
        m = len(matrix)
        n = len(matrix[0])
        f.write(f"{m} {n}\n")
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")

# Đọc ma trận từ file
def read_matrix(filename):
    with open(filename, 'r') as f:
        m, n = map(int, f.readline().split())
        matrix = []
        for _ in range(m):
            row = list(map(float, f.readline().split()))
            matrix.append(row)
    return matrix

# Nhân 2 ma trận
def multiply_matrix(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Kiểm tra điều kiện nhân
    if n != len(B):
        return None

    C = [[0]*p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


# ================= MAIN =================
args = sys.argv

# Trường hợp 2 tham số: tạo 2 ma trận
if len(args) == 3:
    for filename in args[1:3]:
        m = int(input(f"Nhập số dòng m cho {filename}: "))
        n = int(input(f"Nhập số cột n cho {filename}: "))

        matrix = [[round(random.uniform(0, 10), 2) for _ in range(n)] for _ in range(m)]
        write_matrix(filename, matrix)

        print(f"Tạo xong file chứa ma trận: {filename}")

# Trường hợp 3 tham số: nhân ma trận
elif len(args) == 4:
    file1, file2, file3 = args[1], args[2], args[3]

    A = read_matrix(file1)
    B = read_matrix(file2)

    C = multiply_matrix(A, B)

    if C is None:
        print("Không thể nhân hai ma trận!")
    else:
        write_matrix(file3, C)
        print(f"Đã lưu ma trận kết quả vào {file3}")

else:
    print("Sai số lượng tham số dòng lệnh!")
