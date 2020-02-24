# It means inherit something to a class
class A:
    def feature1(self):
        print('Feature 1 iis ON')
    def feature2(self):
        print('Feature 2 iis ON')

class B:
    def feature3(self):
        print('Feature 3 iis ON')
    def feature4(self):
        print('Feature 4 iis ON')

a1=A()
b1=B()
b1.feature3
b1.feature4