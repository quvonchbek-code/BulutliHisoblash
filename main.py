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

def dec_to_hex(n):
    HEX = "0123456789ABCDEF"
    res = ""
    x = n
    while x > 0:
        res = HEX[x % 16] + res
        x //= 16
    return res
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
for i in range(n):
    print(fibonacci(i), end=" ")

n = int(input("10-lik son kiriting: "))

print("2-lik:", dec_to_bin(n))
print("8-lik:", dec_to_oct(n))
print("16-lik:", dec_to_hex(n))
