# Object Oriented Programming
import math
import torch

"""
Question 1
"""
class Softmax:
    def __init__(self, data):
        self.data = data
    def softmax(self):
        result = []
        expx = []
        for i in self.data:
            expx.append(math.exp(i))
        for i in expx:
            result.append(i/sum(expx))
        return torch.tensor(result)
    def softmax_table(self):
        c = max(self.data)
        result = []
        expxc = []
        for i in self.data:
            expxc.append(math.exp(i - c))
        for i in expxc:
            result.append(round(i/sum(expxc), 4))
        return torch.tensor(result)
data = torch.tensor([1,2,3])
softmax = Softmax(data)
print(softmax.softmax())
print(softmax.softmax_table())

"""
Question 2
a Cài đặt các class Student, Doctor, và Teacher theo mô tả trên. Thực hiện phương thức
describe() method để in ra tất cả thông tin của các object.
"""

class Student():
    def __init__(self, name, yob, grade, job="Student"):
        self.job = job
        self.grade = grade
        self.name = name 
        self.yob = yob
    def describe(self):
        print(f'{self.job} - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}')
        
class Doctor():
    def __init__(self,name, yob, specialist, job="Doctor"):
        self.job = job
        self.specialist = specialist
        self.name = name 
        self.yob = yob
    def describe(self):
        print(f'{self.job} - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}')

class Teacher():
    def __init__(self, name, yob, subject, job = 'Teacher'):
        self.job = job
        self.subject = subject
        self.name = name 
        self.yob = yob
    def describe(self):
        print(f'{self.job} - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}')

student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()

"""
b Viết add_person(person) method trong Ward class để add thêm một người mới với nghề
nghiệp bất kỳ (student, teacher, doctor) vào danh sách người của ward. Tạo ra một ward
object, và thêm vào 1 student, 2 teacher, và 2 doctor. Thực hiện describe() method để in ra
tên ward (name) và toàn bộ thông tin của từng người trong ward.
"""

class Ward:
    def __init__(self, name):
        self.name = name
        self.ward_list = []
    def add_person(self, obj):
        self.ward_list.append(obj)
    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.ward_list:
            person.describe()
    def count_doctor(self):
        count = 0
        for person in self.ward_list:
            if person.job.lower() == 'doctor':
                count += 1
        return count
    def sort_age(self):
        self.ward_list.sort(key=lambda x: x.yob)
        return self.ward_list
    def count_average_age(self):
        sum = 0
        count = 0
        for person in self.ward_list:
            if person.job.lower() == 'teacher':
                sum += person.yob
                count += 1
        return sum/count

ward1 = Ward(name = "Ward1")

student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1945, specialist="Endocrinologists")

ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

ward1.describe()

"""
c Viết count_doctor() method để đếm số lượng doctor trong ward.
"""
print(f"\nNumber of doctors: {ward1.count_doctor()}")

"""
d Viết sort_age() method để sort mọi người trong ward theo tuổi của họ với thứ tự tăng dần.
(hint: Có thể sử dụng sort của list hoặc viết thêm function đều được)
"""
print("\nSorted by age:")
ward1.sort_age()
ward1.describe()

"""
e Viết compute_average() method để tính trung bình năm sinh của các teachers trong ward.
"""
print(f"\nAverage age of teachers: {ward1.count_average_age()}")
