import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Nhập n
n = int(input("Nhập n: "))

# Kiểm tra
if is_prime(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không là số nguyên tố")
    
    # Tìm số nguyên tố nhỏ hơn gần nhất
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            print("Số nguyên tố bé hơn gần nhất:", i)
            break
