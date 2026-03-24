def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(day, month, year):
    if month < 1 or month > 12 or day < 1:
        return False

    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    return day <= days_in_month[month - 1]

def day_of_week(day, month, year):
    # Công thức Zeller
    a = (14 - month) // 12
    y = year - a
    m = month + 12 * a - 2

    dow = (day + y + y//4 - y//100 + y//400 + (31*m)//12) % 7
    return dow

def print_day_name(dow):
    days = ["Chủ nhật", "Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7"]
    return days[dow]


# ================= MAIN =================
d, m, y = map(int, input("Nhập ngày, tháng, năm: ").split())

if is_valid_date(d, m, y):
    print("Hợp lệ")
    dow = day_of_week(d, m, y)
    print(print_day_name(dow))
else:
    print("Không hợp lệ")
