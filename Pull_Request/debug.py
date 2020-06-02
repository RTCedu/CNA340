a = int(input())
b = int(input())
c = int(input())

def lone(a, b, c):
    if a == b and b != c:
        return c

    elif a == c and a != b:
        return b

    elif b == c and a != b:
        return a

    elif a == b and a == c and b == c:
        return 0

    else:
        return a+b+c
print(lone(a,b,c))
