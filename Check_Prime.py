import math
arr = list(map(int,input("Nhap vao:").split()))

arr_new = sorted(arr)

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s*s ==x

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square (5*n*n -4)
count = 0

for x in arr_new:
    if is_fibonacci(x):
        count += 1

print(arr_new)
print("So luong so Fibonacci la:", count)