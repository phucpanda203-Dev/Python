import math

# ================== HÀM XỬ LÝ ==================

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))
print(is_fibonacci(13))
print(is_perfect_square(121))
# # ================== NHẬP DỮ LIỆU ==================

# arr = list(map(int, input("Nhap vao day so: ").split()))

# # ================== MENU ==================

# while True:
#     print("\n===== MENU =====")
#     print("1. Sap xep day so")
#     print("2. Dem so Fibonacci")
#     print("3. Dem so nguyen to")
#     print("4. Liet ke so Fibonacci")
#     print("5. Liet ke so nguyen to")
#     print("6. Tim max / min")
#     print("0. Thoat")

#     choice = input("Chon chuc nang: ")

#     if choice == "1":
#         print("Day sau khi sort:", sorted(arr))

#     elif choice == "2":
#         count = sum(1 for x in arr if is_fibonacci(x))
#         print("So luong Fibonacci:", count)

#     elif choice == "3":
#         count = sum(1 for x in arr if is_prime(x))
#         print("So luong so nguyen to:", count)

#     elif choice == "4":
#         fib_list = [x for x in arr if is_fibonacci(x)]
#         print("Cac so Fibonacci:", fib_list)

#     elif choice == "5":
#         prime_list = [x for x in arr if is_prime(x)]
#         print("Cac so nguyen to:", prime_list)

#     elif choice == "6":
#         print("Max:", max(arr))
#         print("Min:", min(arr))

#     elif choice == "0":
#         print("Thoat chuong trinh")
#         break

#     else:
#         print("Lua chon khong hop le!")