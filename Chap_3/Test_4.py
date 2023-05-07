# init value
n, k = map(int, input().split())
res = 0

while True:
    if n < k:
        break
    remain = n % k
    n -= remain
    res += remain

    quot = n // k
    n = quot
    res += 1

res += (n-1)

# Print Result
print(res)