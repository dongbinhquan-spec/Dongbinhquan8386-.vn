def selection_sort(a, n, i=0):
    # Điều kiện dừng
    if i >= n - 1:
        return

    # Tìm vị trí phần tử nhỏ nhất từ i đến n-1
    min_index = i
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j

    # Hoán đổi phần tử nhỏ nhất với a[i]
    a[i], a[min_index] = a[min_index], a[i]

    # Gọi đệ quy cho phần còn lại của mảng
    selection_sort(a, n, i + 1)


# Chương trình chính
arr = [3, 5, 4, 6, 7, 1, 2]
n = len(arr)

print("Mảng gốc:", arr)

selection_sort(arr, n)

print("Mảng tăng:", arr)
