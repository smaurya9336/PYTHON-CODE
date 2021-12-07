#Constructor
class Mobile:
    def __init__(self,m,v=80):
        self.model=m
        self.volumn=v
    def show_model(self,p):
        price=p #Local Variable
        print("Model:",self.model,"and Price",price)
        print("Volumn:",self.volumn)
#Passing Argument to contructor
#realme=Mobile('RealMe X')
realme=Mobile('RealMe',50)

#Accessing Method from outside class
realme.show_model(1000)
print()
redmi=Mobile('Redmi 7s',50)
realme.show_model(2000)




