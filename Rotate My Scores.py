def reverse_scores(scores):
    left = 0
    right = len(scores) - 1
    while left < right:
        scores[left], scores[right] = scores[right], scores[left]
        left += 1
        right -= 1
    return scores
def reverse_in_groups(scores, group_size):
    i = 0
    while i < len(scores):
        left = i
        right = min(i + k - 1, len(scores) - 1)
        while left < right:
            scores[left], scores[right] = scores[right], scores[left]
            left += 1
            right -= 1
        i += k
    return scores
def left_rotate_one(scores):
    if len(scores) == 0:
        return scores
    first = scores[0]
    for i in range(len(scores) - 1):
        scores[i] = scores[i + 1]
    scores[-1] = first
    return scores
def left_rotate_n(scores, n):
    if len(scores) == 0:
        return scores
    n = n % len(scores)
    for _ in range(n):
        left_rotate_one(scores)
        return scores
def find_leaders(scores):
    leaders = []
    if len(scores) == 0:
        return leaders
    max_from_right = scores[-1]
    leaders.append(max_from_right)
    for i in range(len(scores) - 2, -1, -1):
        if scores[i] >= max_from_right:
            max_from_right = scores[i]
            leaders.append(scores[i])
    leaders.reverse()
    return leaders
scores = list(map(int, input("Enter scores: ").split()))
print("\n Original Scores:", scores)
k = int(input("Enter group size for reversal: "))
group_reversed_scores = reverse_in_groups(scores.copy(), k)
print("\n Scores Reversed in Groups of", k, ":", group_reversed_scores)
print("\n1. Reversed Scores:", )
print(reverse_scores(scores.copy()))
gorup = int(input("Enter group size for reversal: "))
print("\n2. Scores Reversed in Groups of", gorup, ":", )
print(reverse_in_groups(scores.copy(), gorup))
print("\n3. Scores after Left Rotation by 1:", )
print(left_rotate_one(scores.copy()))
n = int(input("Enter number of left rotations: "))
print("\n4. Scores after Left Rotation by", n, ":", )
print(left_rotate_n(scores.copy(), n))
print("\n5. Leaders in the Scores:", )
print(find_leaders(scores.copy()))