n = int(input("Enter the number of elements in the array:"))
arr = []
print("Enter the elements of the array:")
for i in range(n):
    element = int(input())
    arr.append(element)
print("Original array:", arr)
start = 0
end = n-1
while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1
print("Reversed array:", arr)