epsilon = 1.0
one = 1.0

while 1+epsilon != 1:
    print(f"Epsilon = {epsilon}")
    epsilon/=2
print(f"Epsilon = {epsilon}")

if 1+epsilon == 1:
    print("Yes\n")
else:
    print("No")