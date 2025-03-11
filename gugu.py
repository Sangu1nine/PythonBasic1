# 구구단
def gugu (a,b):
    return f"{a} x {b} = {a*b:2}"

for a in range(1, 10):
    print(" | ".join(f"{gugu(a, b)}" for b in range(1, 10)))
