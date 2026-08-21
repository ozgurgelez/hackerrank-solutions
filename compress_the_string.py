from itertools import groupby

s = input().strip()

for key, group in groupby(s):
    print((len(list(group)), int(key)), end=" ")