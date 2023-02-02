d={n:n*n for n in range(1,5)}
print(d)

#calculating product price for 5 units
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price)in
     old.items()}
print(new)


#with checks
real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items()
     if age>20}
print(now)


#create a list with 8 customers names display a  dictionary which has customers names along with discounts for them from a particular shop
import random
cust=["susmitha","harshi","manasa","ammu","yamini"]
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)


#create a list1 with student names and list2 with student marks and create a dictionary along with their percentage
list1=['daya','manasa','harshi','ammu','yamini']
list2=[53,68,70,80,83]
per=[] 
for i in list2:
    p=(i*100)/500
    per.append(p)
dict={keys:values for (keys,values) in zip(list1,per)}
print(dict)

#student names,marks/out of 500
#5 subjects-dictionary
#with names and their percentage
import random
student_names=list(map(str,input("enter names:")))
marks=[]
for i in student_names:
   a=(random.randint(300,500)/500)*100
   marks.append(a)
dict={x:y for (x,y) in zip (student_names,marks)}
print(dict)






