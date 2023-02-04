def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
        return sum
    n=int(input("enter the number"))
    res=digits(n)
    print(res)
    '''n=321
rem=321%10 ------1
0+1----sum ---1
n=321//10 ----32
rem=32%10-----2
sum------1+2----3
n=32//10-----3
rem=3%10------3
sum=3+3------6
n=3//10-----0
