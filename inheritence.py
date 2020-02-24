# It means inherit something to a class
class A:
    def feature1(self):
        print('Feature 1 iis ON')
    def feature2(self):
        print('Feature 2 iis ON')

class B(A): #----Single-Level----
    def feature3(self):
        print('Feature 3 iis ON')
    def feature4(self):
        print('Feature 4 iis ON')

class C(B): #----Multi level----
    def feature5(self):
        print('Feature 5 is ON')

class D:
    def feature6(self):
        print('Feature 6 is ON')
    def feature7(self):
        print('Featurre D,7 is ON')

class E(C,D): #----Multiple level----
    def feature10(self):
        print('Feature E,10 is ON')

a1=A() #--here 'A' is a constructor of 'a1' ---
b1=B()
a1.feature1()
a1.feature2()
b1.feature3()
b1.feature4()
b1.feature1()
c1=C()
c1.feature5()
c1.feature3()
c1.feature1()
e1=E()
e1.feature4()
e1.feature1()
e1.feature10()
e1.feature6()