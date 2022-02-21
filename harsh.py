# write a program to print star pattern in H Shape
for row in range(7):
    for col in range(5):
        if(col==0 or col==4) or (row==3 and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")  
    print()
# write a program to print star pattern in A Shape
for row in range(7):
    for col in range(5):
        if((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

# write a program to print star pattern in R Shape
for row in range(7):
    for col in range(5):
        if(col==0) or ((row==0) or row==3) and (col>0 and col<4) or ((col==4) and (row>0 and row<3)) or (row-col==2):
            print("*",end="")
        else:
            print(end=" ")
    print()

# write a program to print star pattern in S Shape
for row in range(7):
    for col in range(5):
        if(row==0 or row==3 or row==6) and (col>0 and col<4) or ((col==0) and (row>0 and row<3)) or ((col==4) and (row>3 and row<6)) or (col==0 and row==6) or (row==0 and col==4):
           print("*",end="")
        else:
            print(end=" ")
    print() 
# write a program to print star pattern in H Shape
for row in range(7):
    for col in range(5):
        if(col==0 or col==4) or (row==3 and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")  
    print()

