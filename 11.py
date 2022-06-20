n = int(input())
plan = []
ans = "Yes"
sec = 0
loc = 0
for i in range(n):
    plan.append(list(map(int, input().split())))
for i in range(n):
    sec = plan[i][0] - sec
    loc = abs(plan[i][1] + plan[i][2] - loc)
    if sec < abs(loc) or (sec - loc) % 2 == 1:
        ans = "No"
        break
print(ans)