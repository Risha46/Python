stones = "aabbcd"
jewels = "ab"
ans = 0
for i in stones:
    if i in jewels:
        ans = ans + 1
print(ans)