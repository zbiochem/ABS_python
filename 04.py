n = int(input())
a = list(map(int, input().split()))
a = list(map(bin, a))
a = list(map(lambda x:x[2:], a))
ans = []
for i in a:
    ans.append(int(len(i)) - int(i.rfind("1")) - 1)
ans.sort()
print(ans[0])