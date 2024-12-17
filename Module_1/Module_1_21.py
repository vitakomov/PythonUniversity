grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
averages_marks = {}
for i in range (0,len(students_list)): averages_marks.update({students_list[i] : (sum(grades[i]) / len(grades[i]))})
print(averages_marks)
