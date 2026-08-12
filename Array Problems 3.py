arr = [ 1,1,0,1,1,0,1,1]
streak = 0
print("\n==== Part 1 : Streak Counter ====")
for num in arr:
    if num == 1:
        streak += 1
    else:
        streak = 0
    print("Current Value:" , num,"Streak:" , streak)
streak = 0
best_streak = 0
print("\n==== Part 2 : Maximum Consecutive Ones ====")
for num in arr:
    if num == 1:
        streak += 1
        if streak > best_streak:
            best_streak = streak
    else:
        streak = 0
    print("Maximum Consecutive Ones:" , best_streak)
arr = [0,1,0,3,12,0,5,0,7]
write = 0
print("\n==== Part 3 : Move Zeroes ====")
print("Before" , arr)
for read in range(len(arr)):
    if arr[read] != 0:
        arr[write],arr[read] = arr[read],arr[write]
        write += 1
    print("After" , arr)
non_zero_count = write
zero_count = len(arr) - write
print("\nPart 4 : Final Sepration")
print("Write pointer" , write)
print("Non-zero elements:" , non_zero_count)
print("Zero elements:" , zero_count)