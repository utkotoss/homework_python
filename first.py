A = int(input())
B = int(input())

def NOD(a, b) :
    if (b > a) :
        c = a
        a = b
        b = c
    a %= b
    if (a != 0) :
        return NOD(a, b)
    else :
        return b

print("your answer is here  -> ", NOD(A, B))