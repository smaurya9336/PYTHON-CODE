#single inheritance
class Father:
    money=1000
    def show(self):
        print("Parent class Instance method")

    @classmethod
    def showmoney(cls):
        print("Parent class class method:",cls.money)

    @staticmethod
    def stat():
        a=20
        print("Parent class static method:",a)

class Son(Father):
    def disp(self):
        print("Child class Instance method")


s=Son()
s.disp()
s.show()
s.showmoney()
s.stat()
print()
f=Father()
f.show()
f.showmoney()
f.stat()