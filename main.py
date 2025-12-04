def dec_to_bin(n):
    res = ""
    x = n
    while x > 0:
        res = str(x % 2) + res
        x //= 2
    return res


n = int(input("10-lik son kiriting: "))

print("2-lik:", dec_to_bin(n))
