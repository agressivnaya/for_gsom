semester_work = 40 #integer assigned value
assignment_amount = int (input ('The number of assignments: ')) #input string converted to the integer
max_grade = assignment_amount * 5
print ('The maximum score is:', max_grade)
assignment_number = 1
grades_list = [] #empty list created
while assignment_number <= assignment_amount:
    print('Your grade for assignment №', assignment_number, ':')
    grade = int (input()) #input string converted to the integer
    grades_list.append (grade) #input added to the list
    assignment_number +=1
print ('Your grades are:', grades_list)
semester_grade = sum (grades_list)/max_grade * 40 #float calculation
print ('Your semester grade is:', semester_grade, '% out of 40%')