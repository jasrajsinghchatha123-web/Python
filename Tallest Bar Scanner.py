def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
def build_left_max(heights):
    n = len(heights)
    left_max = [0] * n
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])
    return left_max
def build_right_max(heights):
    n = len(heights)
    right_max = [0] * n
    right_max[-1] = heights[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])
    return right_max
def trapped_water(heights):
    if not heights:
        if len(heights) == 0:
            return 0
        left_max = build_left_max(heights)
        right_max = build_right_max(heights)
        water = 0
        for i in range(len(heights)):
            water += min(left_max[i], right_max[i]) - heights[i]
        return water
print( "==== Tallest Bar Scanner ==== ")
prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))
profit = max_profit(prices)
heights = list(map(int, input("Enter heights separated by spaces: ").split()))
left_max = build_left_max(heights)
right_max = build_right_max(heights)
water = trapped_water(heights)
print("\n Bar Heights" , heights)
print("\n Left Tallest Bar:" , left_max)
print("\n Right Tallest Bar:" , right_max)
print("Total Trapped Rain-Water:" , water)