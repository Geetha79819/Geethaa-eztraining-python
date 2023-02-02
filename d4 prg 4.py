#iteration logic:
s=input("enter: ")
char=input("enter: ")
for i in s:
    if i==char:
        flag=1
        break
    else:
        flag=0
if flag==1:
   print("present")
else:
   print("not present")
