N = int(input().strip())
Q: list[int] = list(map(int, input().strip().split()))
C: list[int] = list(map(int, input().strip().split()))
A, B = map(int, input().strip().split())

if A < B:
    D: list[int] = []
    for i in C:
        d = int(A + (i * (B - A)) / 255)
        D.append(d)
    print(sum(d * q for d, q in zip(D, Q)))
else:
    print(sum(q * A for q in Q))
