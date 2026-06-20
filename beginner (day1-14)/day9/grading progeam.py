student_score={
    "harry":81,
    "ron":78,
    "hermaine":99,
    "draco":74,
    "Neville":62,
}

student_grades={}
for student in student_score:
    score= student_score[student]
    if (score>=91) and (score <=100):
        student_grades[student]="outstanding"
    
    elif (score>=80) and (score<=90):
        student_grades[student]="Exceeds Expectation"
           
    elif (score>=70) and (score<80):
        student_grades[student]="Acceptable"
    
    elif  (score<70):
        student_grades[student]="Fail"
    else:
        print("wrong input")       
       
print(student_grades)