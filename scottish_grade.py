# what grade do i need to score in my remaining courses to graduate with a good grade

number_of_semesters = input("how many semesters do you have left ?")

total_points = 0

# previous semester
semester_1_grade_base = []
previous_courses = int(input("How many courses did you take in your previous semester? \n"))

previous_semester_number_of_courses = previous_courses

grade_1 = input("What was your grade in your most difficult course? \n")
semester_1_grade_base.append(grade_1)
previous_semester_number_of_courses -= 1


while previous_semester_number_of_courses != 0:
    grade_next = input("What was your grade in your next course? \n")
    semester_1_grade_base.append(grade_next)
    previous_semester_number_of_courses -= 1



print(semester_1_grade_base)



course_1 = input("How many courses are you taking in the next semester ?")

if number_of_semesters > 1 :
    course_2 = input("How many courses are you taking in the further semester?")




