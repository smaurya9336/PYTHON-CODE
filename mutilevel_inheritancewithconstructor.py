#multilevel Inheritance with constructor
class Father:
    def __init__(self):
        print("Father class constructor")

    def showF(self):
        print("Father class method")

class Son(Father):
    def __init__(self):
        print("Son class constructor")

    def showS(self):
        print("Son class method")

class GrandSon(Son):
    def __init__(self):
        print("GrandSon class constructor")
    
    def showG(self):
        print("GrandSon class method")


g=GrandSon()
g.showG()
g.showF()
g.showS()
                