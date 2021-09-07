height_of_students = list(map(int, input("Enter the height of the students in cm").split(", ")))
total_students = len(height_of_students)
total_height_sum = 0
for height in height_of_students:
    total_height_sum += height
student_average = round((total_height_sum // total_students), 2)
print(f"Average height of the students is:{student_average}")
