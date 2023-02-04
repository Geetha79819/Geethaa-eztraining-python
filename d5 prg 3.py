def sample():
    print("great day")
    print("happy time")


sample()
print("today")
sample()

#without argument,without return value
def multi():
    n1=int(input("number"))
    n2=int(input("number"))
    n3=int(input("number"))
    sum=n1+n2+n3
    print(sum)

multi()

#without argument,with return value
def multi():
    x=int(input("number"))
    y=int(input("number"))
    z=int(input("number"))
    prod=x*y*z
    return prod
res=multi()
print(res)

#with argument,with return value
def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)

multi(3,4,5)
def multi(a,b,c):
    prod=a*b*c
    print(prod)

n1=int(input("enter 1: "))
n2=int(input("enter 2: "))
n3=int(input("enter 3: "))
multi1(n1,n2,n3)
