prices = [7, 1, 5, 3, 6, 4]
profit = 0
for i in range(1 , len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]
print("Part 1 : Stock Biuy-Sell")
print("Maximum Profit:", profit)
heights = [ 4 , 2 , 0 , 3 , 2 , 5 ]
left_tallest = [0] * len(heights)
left_tallest[0] = heights[0]
print("\nPART 2: Left Tallest")
print("Heights:", heights)
print("Left Tallest:", left_tallest)
for i in range(1 , len(heights)):
    left_tallest[i] = max(left_tallest[i - 1] , heights[i])
right_tallest = [0] * len(heights)
right_tallest[-1] = heights[-1]
for i in range(len(heights) - 2 , -1 , -1):
    right_tallest[i] = max(right_tallest[i + 1] , heights[i])
print("\nPART 3: Right Tallest")
print("Right Tallest:", right_tallest)
total_water = 0
for i in range(len(heights)):
    water = min(left_tallest[i] , right_tallest[i]) - heights[i]
    total_water += water
print("\nPART 4: Total Water Trapped")
print("Total Water Trapped:", total_water)