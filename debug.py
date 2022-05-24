#function given in the question
def lone_sum(a, b, c):
    #sum contain the sum of 3 values in a,b and c
    sum = a + b + c
    if a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif a == b and a == c and b == c:
        return 0
    else:
        return sum

#input the values of a, b and c from the user
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
#function call
print(lone_sum(a,b,c) )
