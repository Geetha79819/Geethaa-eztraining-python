l=list(map(int,input("enter").split()))
product = 1
sum = 0
for i in 1:
    product=product*i
    sum=sum+i
if(product<750):
    print(product)
else:
    print(sum)
    
