def f1(n):
    if n > 5:
        return n * 3
    else:
        return 0

def coolFn(x = 3) :
    q = 0
    for i in range(x):
        q = q + i
    return q

if __name__ == "__main__":
    print coolFn(f1(3**3))
