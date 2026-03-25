arr = [3,1,5,7,2,9]

x = int(input("Nhap so can tim: "))

found = False

for i in range(len(arr)):
    if arr[i] == x:
        print("Tim thay X tai vi tri", i ,"trong mang")
        found = True
        break

if not True:
    print ("Khong tim thay X")