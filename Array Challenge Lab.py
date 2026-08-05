print("===== PART 1 : Reverse Entire List =====")
arr = list(map(int, input("Enter elements: ").split()))
start = 0
end = len(arr) - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print("Reversed List:", arr)

print("\n===== PART 2 : Reverse in Groups of 3 =====")
arr = list(map(int, input("Enter elements: ").split()))
group_size = 3
i = 0
while i < len(arr):
    left = i
    right = min(i + group_size - 1, len(arr) - 1)
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    i += group_size
print("After Group Reversal:", arr)

print("\n===== PART 3 : Left Rotate List =====")
arr = list(map(int, input("Enter elements: ").split()))
n = int(input("Enter number of left rotations: "))
length = len(arr)
if length > 0:
    n = n % length
    for _ in range(n):
        temp = arr[0]
        for i in range(length - 1):
            arr[i] = arr[i + 1]
        arr[length - 1] = temp
print("After Left Rotation:", arr)

print("\n===== PART 4 : Leaders in the List =====")
arr = list(map(int, input("Enter elements: ").split()))
leaders = []
if len(arr) > 0:
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(arr[i])
leaders.reverse()
print("Leaders:", leaders)