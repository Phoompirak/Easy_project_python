def IS_prime(n, n_end):
    if len(n) == 2:
        for x in n:
            if x == 1:
                continue
            if x == n_end:
                return True


def sum_prime(x, y):
    total_prime = []
    for i in range(x, y+1):
        total_factors = []
        if x < 2:
            x = 2
        for j in range(1, i+1):
            if i%j == 0:
                total_factors.append(j)

        is_prime = IS_prime(total_factors, i)
        if is_prime:
            total_prime.append(i)

    return sum(total_prime)

x, y = int(input("Insert x :")), int(input("Insert y :"))
print("จำนวนเฉพาะ =", sum_prime(x, y))