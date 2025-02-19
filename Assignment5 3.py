def next_permutation(w):
    w = list(w)
    for i in range(len(w) - 2, -1, -1):
        if w[i] < w[i + 1]:
            for j in range(len(w) - 1, i, -1):
                if w[j] > w[i]:
                    w[i], w[j] = w[j], w[i]
                    w = w[:i + 1] + sorted(w[i + 1:])
                    return ''.join(w)
    return "no answer"

t = int(input())
for _ in range(t):
    print(next_permutation(input()))
