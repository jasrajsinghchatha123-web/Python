arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
if len(arr) < 2:
    print("Array must contain at least two elements.")
else:
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        print("There is no second largest element.")
    else:
        print("Second largest element:", second_largest)