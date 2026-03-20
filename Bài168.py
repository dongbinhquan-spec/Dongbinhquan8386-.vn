from datetime import datetime

# Định nghĩa lớp Book (giống struct trong C)
class Book:
    def __init__(self, title, isbn, author, publisher, date):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.publisher = publisher
        self.date = date

    def display(self):
        print(self.title)
        print(self.author)
        print(self.publisher)
        print(f"[update: {self.date.strftime('%d-%m-%Y')}]")

# Danh sách lưu các sách
books = []

# Nhập dữ liệu
while True:
    print("\nNhập thông tin sách:")
    title = input("Tựa: ")
    isbn = input("ISBN: ")
    author = input("Tác giả: ")
    publisher = input("NXB: ")
    
    # nhập ngày
    day = int(input("Ngày: "))
    month = int(input("Tháng: "))
    year = int(input("Năm: "))
    date = datetime(year, month, day)

    books.append(Book(title, isbn, author, publisher, date))

    cont = input("Tiếp (y/n)? ")
    if cont.lower() != 'y':
        break

# Tìm kiếm theo ISBN
search_isbn = input("\nNhập ISBN cần tìm: ")

found = False
print("\nKết quả tìm:")
for book in books:
    if book.isbn == search_isbn:
        book.display()
        found = True
        break

if not found:
    print("Không tìm thấy sách!")
