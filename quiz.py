q1=""" Is Python case sensitive when dealing with Identifiers?
 a.Yes
 b.No
 c.Machine Dependent
 d.None"""
q2=""" Which of the following is not a keyword?
 a.eval
 b.assert
 c.local
 d.pass"""
q3="""" Which one of these is floor division?
 a./
 b.//
 c.%
 d.None"""
q4=""""What is the output of this 3*1**3?
 a.27
 b.9
 c.3
 d.1"""
q5="""""a"+"bc"=?
 a.a
 b.bc
 c.bca
 d.abc
 """
question ={q1:"a",q2:"a",q3:"b",q4:"c",q5:"d"}
name=input("Enter your name:--")
print("hello!",name,"Welcome to the quiz world")
score=0
for i in question:
    print()
    print(i)
    flag1=input("Do you want to skip this question (yes/no):")
    if flag1=="yes":
        continue
    ans=input("Enter the answer (a/b/c/d):")
    if ans==question[i]:
        print("correct answer,you got 1 point")
        score=score+1
        print("current score is:",score)
    else:
        print("wrong answer,you lost 1 point")
        print("current score is:",score)
    flag2=input("Do you want to quit(yes/no):")
    if flag2=="yes":
        break
print("Final score is:",score)