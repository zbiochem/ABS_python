n = int(input())
a = list(map(int, input().split()))
ans = 0
a.sort(reverse = True)
for i in range(len(a)):
    if i % 2 == 0:
        ans += a[i]
    else:
        ans -= a[i]
print(ans)
