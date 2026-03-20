import math

# Nhập tọa độ điểm A
xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))

# Nhập tọa độ điểm B
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))

# Tính khoảng cách
AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

# In kết quả
print("Khoảng cách AB =", AB)
