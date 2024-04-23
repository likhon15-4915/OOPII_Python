class Student:

    def __init__(Self,name,cgpa,id):
        Self.Name = name
        Self.Cgpa = cgpa
        Self.Id = id
    def Status(Self):
        print("Currenty Studying")
    def details(Self):
        print(Self.Name,Self.Cgpa,Self.Id)

sty1 = Student("Likhon", 3.5,"221-15-4915")
sty2 = Student("Ain", 3.75, "22-15-4693")
sty3 = Student("Taohyd", 3.85, "221-15-5288")

sty1.details()
sty1.Status()
print("")
sty2.details()
sty2.Status()
print("")
sty3.details()
sty3.Status()
