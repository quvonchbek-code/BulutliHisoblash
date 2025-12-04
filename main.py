def dec_to_bin(n):
    res = ""
    x = n
    while x > 0:
        res = str(x % 2) + res
        x //= 2
    return res

def dec_to_oct(n):
    res = ""
    x = n
    while x > 0:
        res = str(x % 8) + res
        x //= 8
    return res



n = int(input("10-lik son kiriting: "))

print("2-lik:", dec_to_bin(n))
print("8-lik:", dec_to_oct(n))
