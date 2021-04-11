
students_list = ["Paul", "Louis", "Mathieu", "Bastien"]

with open("students.txt", "w+") as file:
    for students in students_list:
        file.write(students + "\n")
    file.close()