arr = [ 2, -3 , 4 , 5 , -2 , 3 , -6 , 4]
slice1 = arr[0:3]
slice2 = arr[2:6]
slice3 = arr[4:8]
print(" Part 1 : SubArrays")
print("Array:" , arr)
print("\nSlice 1:" , slice1)
print("Sum:" , sum(slice1))
print("\nSlice 2:" , (slice2))
print("Sum:" , sum(slice2))
print("\nSlice 3:" , (slice3))
print("Sum:" , sum(slice3))
print("\n\n Part 2 : Running Sum With Reset")
running_sum = 0
for value in arr:
    for value in arr:
        running_sum += value
        print("Element" , value , "Running Sum:" , running_sum)
print("\n\n Part 3 : Maximum SubArray Sum")
running_sum = 0
best = 0
for value in arr:
    running_sum += value 
if running_sum < 0:
    running_sum = 0
if running_sum > best:
    best = running_sum
print("Array:" , arr)
print("Maximum SubArray Sum:" , best)
print("\n\n Part 4 : Complete Kadane's Algorithm")
arr2 = [-8 , 3 , -2 , 5 , -1 , 6 , -7 , 4 , -3 , 2]
running_sum = 0
best = arr2[0]
print("Array:" , arr)
for value in arr2:
    running_sum += value
    if running_sum < 0:
        running_sum = 0
    if running_sum > 0:
        best = running_sum
    print("Element:" , value , "Running Sum:" , running_sum , "Best" , best)
print("\n Maximum SubArray Sum:" , best)