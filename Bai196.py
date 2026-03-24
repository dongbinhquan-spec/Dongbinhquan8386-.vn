# Kiểm tra ký tự thường
def islower(c):
    return 1 if 'a' <= c <= 'z' else 0

# Chuyển sang chữ hoa
def toupper(c):
    if 'a' <= c <= 'z':
        return chr(ord(c) - 32)
    return c

# Tính phần trăm a trên b
def percent(a, b):
    if b == 0:
        return None
    return (a / b) * 100


# ================= TEST =================
c = 'c'
print(f"'{c}' viet hoa la '{toupper(c)}'")

a = 123
b = 12345
p = percent(a, b)

if p is not None:
    print(f"{a} la {p:.6f}% cua {b}")
else:
    print("Không thể tính (b = 0)")
