ans = "YES"
s = input()[::-1]
while s:
    if s[:6] == "resare":
        s = s[6:]
    elif s[:7] == "remaerd":
        s = s[7:]
    elif s[:5] == "esare":
        s = s[5:]
    elif s[:5] == "maerd":
        s = s[5:]
    else:
        ans = "NO"
        break
print(ans)