arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
maximum = arr[0]
minimum = arr[0]
for num in arr:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum:", maximum)
print("Minimum:", minimum)