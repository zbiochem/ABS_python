n, a, b = map(int, input().split())
ans = 0
def sum_(x):
    s = str(x).zfill(5)
    if a <= int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]) + int(s[4])<= b:
        return True
    else:
        return False
for i in range(n + 1):
    if sum_(i):
        ans += i
print(ans)