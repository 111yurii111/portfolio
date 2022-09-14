StudentName = ["Max", "Bob"]
StudentMark = [[90,100],[80,90]]
ClassSize = 2
SubjectNo = 2

distinction = 0
merit = 0
Pass = 0
fail = 0

#for every student
for i in range(ClassSize):
    totalmark = 0
    #add every mark to one variable 
    for j in range(SubjectNo):
        totalmark += StudentMark[i][j]

    #divides totalmark by number of subjects for the average
    avgmark = round(totalmark / SubjectNo)

    if avgmark >= 70:
        grade = "distinction"
        distinction += 1

    elif avgmark >= 55:
        grade = "merit"
        merit += 1

    elif avgmark >= 40:
        grade = "pass"
        Pass += 1

    elif avgmark < 40:
        grade = "fail"
        fail += 1

    print(f"Name: {StudentName[i]}")
    print(f"Total mark: {totalmark}")
    print(f"Average mark: {avgmark}")
    print(f"Grade awarded: {grade}\n")


print(f"Number of students with grade awarded distinction : {distinction}")
print(f"Number of students with grade awarded merit : {merit}")
print(f"Number of students with grade awarded pass : {Pass}")
print(f"Number of students with grade awarded fail : {fail}")
