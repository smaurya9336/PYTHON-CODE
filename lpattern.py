from typing import Pattern


#wap  to print alphabetical L Pattern
for row in range(7):
    for col in range(5):
        if col==0 or (row==6 and col>0):
            print("*",end="")
    print()