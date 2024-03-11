Student_Result={"Math":60,"Eng":70,"Phy":85}
print(Student_Result.values())
print(Student_Result.keys())
print(Student_Result.items())

average=(sum(Student_Result.values()))/ len(Student_Result)
print(round(average))
