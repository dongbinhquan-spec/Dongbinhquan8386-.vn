from itertools import combinations

# Nhập chuỗi
s = input("Nhập chuỗi: ")

# Lấy các chữ số
digits = [c for c in s if c.isdigit()]

# Kiểm tra đủ 4 chữ số
if len(digits) < 4:
    print("Không đủ 4 chữ số!")
else:
    max_num = -1

    # Chọn tất cả tổ hợp 4 chữ số theo thứ tự
    for comb in combinations(digits, 4):
        num = int("".join(comb))
        if num > max_num:
            max_num = num

    print("Số lớn nhất còn lại:", max_num)
