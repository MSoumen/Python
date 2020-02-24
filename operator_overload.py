class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        sum1=self.m1+self.m2
        sum2=other.m1+other.m2
        sum3=Student(sum1,sum2)
        return sum3
    
    def __gt__(self,other):
        sum1=self.m1+self.m2
        sum2=other.m1+other.m2
        if sum1>sum2:
            return True
        else:
            return False



s1=Student(5,5)
s2=Student(8,2)
s3=s1+s2        # s3 = Student.__add__(s1,s2)

print(s3.m1,s3.m2)
if s1>s2:
    print('S1 wins')
else:
    print('S2 wins')

    