print("Ex1")
arr1 = [5,2,1,4,9]
sorted_arr1 = sorted(arr1)
print(arr1)
print(sorted_arr1)

print("Ex2")
arr2 = [5,6,3,8,9]
arr2.sort()
print(arr2)
print(arr2)

print("Ex3")
arr3 = [1,2,3,4,5]
arr3.reverse()
print(arr3)

print("Ex4")
arr4 = ["apple", "kiwi", "banana"]
sorted_arr4 = sorted(arr4, key=len)
print(arr4)
print(sorted_arr4)

print("Ex5")
arr5 = [
    {"name":"A","score":"4"},
    {"name":"B","score":"9"},
    {"name":"C","score":"6"}
]
sorted_arr5 = sorted(arr5, key =lambda x: x["score"])
print(arr5)
print(sorted_arr5)
