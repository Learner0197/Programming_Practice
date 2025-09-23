class Student:
    marks={}
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def getname(self):
        return self.name

    def dispdetails(self):
        print("Student Name:",self.name)
        print(self.marks)

    def calcpercent(self):
        total,count=0,0
        for i in self.marks:
            total=total+self.marks[i]
            count+=1
        percent=total//count
        return percent

a=Student("Aman",{"Java":75,"Python":85,"Maths":80,"Effective Communication":65,"Fundamentals of AI":70})
b=Student("Arnav",{"Java":60,"Python":75,"Maths":85,"Effective Communication":75,"Fundamentals of AI":75})
c=Student("Arunesh",{"Java":85,"Python":90,"Maths":90,"Effective Communication":100,"Fundamentals of AI":85})
d=[b,a,c]
d_sort=sorted(d, key=lambda student:student.calcpercent(),reverse=True)
for i in d_sort:
    print({i.getname()},{i.calcpercent()})
highest=d_sort[0]
lowest=d_sort[-1]
print(highest.getname())
print(lowest.getname())
# p={}
# for i in d:
#     p.setdefault(i.getname(),i.calcpercent())
# print("The student with maximum percentage is",max(p))
# print("The student with minimum percentage is",min(p))

