arr1 = [1,1,1,0,1,1,1,0,1,1,1,]
streak = 0
print("\n==== Part 1 : Streak Counter ====")
for num in arr1:
    if num == 1:
        streak += 1
    else:
        streak = 0
    print("Current Value:" , num,"Streak:" , streak)
arr2 = [0,1,1,0,0,1,0,1,1,0,0,1]
streak = 0
best_streak = 0
print("\n==== Part 2 : Maximum Consecutive Ones ====")
for num in arr2:
    if num == 1:
        streak += 1
        if streak > best_streak:
            best_streak = streak
    else:
        streak = 0
    print("Maximum Consecutive Ones:" , best_streak)
print("Array:" , arr2)
print("Maximum Consecutive Ones:" , best_streak)
arr3 = [8,0,4,6,0,2,9,0,1,7,3]
write = 0
print("\n==== Part 3 : Move Zeroes ====")
print("Before" , arr3)
for read in range(len(arr3)):
    if arr3[read] != 0:
        arr3[write],arr3[read] = arr3[read],arr3[write]
        write += 1
    print("After" , arr3)
print("Updated Array:" , arr3)
print("\nPart 4 : Final Separation")
print("Final Write pointer" , write)
print("Non-zero elements:" , write)
print("Zero elements:" , len(arr3) - write)