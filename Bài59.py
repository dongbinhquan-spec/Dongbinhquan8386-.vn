# Danh sách Can và Chi
can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", 
       "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]

chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", 
       "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# Hàm tính Can Chi
def can_chi(year):
    c = can[(year + 6) % 10]
    ch = chi[(year + 8) % 12]
    return c + " " + ch

# Nhập năm
year = int(input("Nhập năm: "))

# Xuất năm âm lịch
print(f"{year} - {can_chi(year)}")

# Tìm năm tiếp theo có cùng Can Chi
next_year = year + 60
print(f"{next_year} - {can_chi(next_year)}")
