arr = [3,1,5,7,2,9]
# Cách 1
x = int(input("Nhap so can tim: "))

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == x:
        print("Tim thay tai:", mid)
        break
    elif arr[mid] < x:
        left = mid + 1
    else:
        right = mid -1
else:
    print("Khong tim thay X")

arr_new = sorted(arr)
print(arr_new)

