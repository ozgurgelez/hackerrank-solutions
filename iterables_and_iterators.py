from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

all_combinations = list(combinations(letters, k))
combinations_with_a = [combo for combo in all_combinations if 'a' in combo]
probability = len(combinations_with_a) / len(all_combinations)
print(f"{probability:.3f}")