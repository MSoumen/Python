class A:
    def __init__(self):
        print('In A__init__')
    def feature1(self):
        print('In A-1 feature')
    def feature2(self):
        print('In A-2 feature')

class B:
    def __init__(self):
        print('In B__init__')
    #    super().__init__()  #-- this super() methid call __init__  and other methods of the super class 

    def feature1(self):
        print('In B-3 feature')
    def feature4(self):
        print('In B-4 feature')

class C(A,B):
    def __init__(self):
        print('In C__init__')
        super().__init__()  #--here this super() methid will call A__init CAZ A is the leftmost superClass
        # This oder maintain is called MRO(Method  Resolution Order)
    def feat(self):
        super().feature1()

# a1=A()
#b1=B()  ##--Here 'B' constractor 1st search for __init__ of class B ...If not found then it goes to SuperClass and find for __init__
c1=C()
c1.feat()
