# arr containing all percentage grades
class_grades = [67,75,76,81,83,86,86,89,90,92]

# var to determine the mean value (avg )of the "class_grades" array
avg_grade = sum(class_grades)/len(class_grades)

# printing the results
print("The class average was",avg_grade,"%")

# function to determine what the average letter grade was and the reward
def donuts(class_grades):
# if statement determining what happens if avg is A
    if avg_grade >= 90:
        print("Congrats, the class average was an A. Everyone get a donut!")
# elif statement determining what happens if avg is B
    elif avg_grade >= 80:
        print("Good job, the class average was a B. Everyone gets 1/2 a donut!")
# elif statement determining what happens if avg is C
    elif avg_grade >= 70:
        print("The class average was C, good effort. Everyone gets 1/3 of a donut!")
# elif statement determining what happens if avg is D
    elif avg_grade >= 60:
        print("The class average was a D, everyone has to give 1/2 donut to Mr. James. At least you tried.")

# calling back the function
donuts(avg_grade)
