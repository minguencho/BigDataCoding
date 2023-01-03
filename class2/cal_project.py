#cal_project.py

#class 선언
#self는 클래스의 변수 참조
class FourCal():
    #생성자
    def __init__(self,first,second):
        self.first = first
        self.second = second    
    def plus(self):
        result = self.first + self.second
        return result
    def minus(self):
        result = self.first - self.second
        return result
    def multiple(self):
        result = self.first * self.second
        return result
    def devide(self):
        result = self.first / self.second
        return result

cal = FourCal(4,2)

print(cal.first, cal.second)
print(cal.plus(),cal.minus(),cal.multiple(),cal.devide())

