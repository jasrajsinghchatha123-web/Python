arr = [2, -3, 4, 5, -2, 3, -6, 4]
print("PART 1: SUBARRAYS")
print("Original Array:", arr)
subarray1 = arr[0:3]
subarray2 = arr[2:6]
subarray3 = arr[4:8]
print("\nSubarray 1:", subarray1)
print("Sum:", sum(subarray1))
print("\nSubarray 2:", subarray2)
print("Sum:", sum(subarray2))
print("\nSubarray 3:", subarray3)
print("Sum:", sum(subarray3))
print("\n\nPART 2: RUNNING ENERGY")
running_sum = 0
for value in arr:
    running_sum += value
    print("Element:", value, "| Running Energy:", running_sum)
    if running_sum < 0:
        print("Energy became negative. Resetting to 0.")
        running_sum = 0
print("\n\nPART 3: BEST ENERGY")
running_sum = 0
best = 0
for value in arr:
    running_sum += value
    if running_sum < 0:
        running_sum = 0
    if running_sum > best:
        best = running_sum
print("Array:", arr)
print("Maximum Subarray Sum:", best)
print("\n\nPART 4: COMPLETE KADANE'S ALGORITHM")
arr2 = [-8, 3, -2, 5, -1, 6, -7, 4, -3, 2]
running_sum = 0
best = arr2[0]
print("Array:", arr2)
for value in arr2:
    running_sum += value
    if running_sum < 0:
        running_sum = 0
    if running_sum > best:
        best = running_sum
    print("Element:", value,
          "| Running Energy:", running_sum,
          "| Best:", best)
print("\nMaximum Subarray Sum:", best)