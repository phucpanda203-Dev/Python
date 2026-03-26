arr = [3,6,4,5]

print("Mang dau tien", arr)

n = len(arr)

for i in range(n):
  for j in range(0, n-i-1):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]
print("Mang sau khi sap xep",arr)
