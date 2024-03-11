Student_Marks = {"Student1": {"Math": 60, "Eng": 70, "Phy": 85},
                 "Student2": {"Math": 65, "Eng": 73, "Phy": 60},
                 "Student3": {"Math": 55, "Eng": 75, "Phy": 78}}

average_marks={}
for name in Student_Marks:
    val=Student_Marks[name].values()
    avg=sum(val)/len(val)
    average_marks[name]=avg
print(average_marks)
