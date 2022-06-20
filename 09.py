n, y = map(int, input().split())
y /= 1000
ans = [-1, -1, -1]
for i in range(int(y / 10) + 1):
    for j in range(int((y - 10 * i) / 5) + 1):
        if y - 9 * i - 4 * j == n:
            ans = [i, j, n - i - j]
            break 
print(ans[0], ans[1], ans[2])