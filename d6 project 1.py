q1="""who is rrr hero?
a.nani
b.prabhas
c.ntr
d.mahesh babu"""
q2="""what is your favourite food?
a.biryani
b.noodles
c.pizza
d.manchuria"""
q3="""what is your favourite food?
a.yellow
b.red
c.blue
d.green"""
q4="""what is your favourite game?
a.kabbadi
b.chess
c.throwball
d.football"""
q5="""what is your favourite kpop group?
a.bts
b.blackpink
c.one direction
d.momoland"""
questions={q1:"c",q2:"a",q3:"c",q4:"b",q5:"a"}
name=input("hi whats your name")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do you want to skip this ques (yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans== questions[i]:
        print("wow!you got one point")
        score=score+1
        print("your current score is:",score)
    else:
        print("wrong answer,u lost 1 mark")
        score=score-1
        print("ur current score is",score)
    flag2=input("do you want to quit? type(yes/no)")
    if flag2=="yes":
        break
    print("your total score is",score)
