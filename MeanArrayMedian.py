arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
n = len(arr)
mean = sum(arr) / n
arr.sort()
if n % 2 == 0:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
else:
    median = arr[n // 2]
print("Mean:", mean)
print("Median:", median)