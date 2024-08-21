a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

def greater(a,b,c):
    if(a>b) and (a>c):
        return("a is greater")
    elif(b>a) and (b>c):
        return("b is greater")
    else:
        print("c is greater")
greater(a, b, c)
