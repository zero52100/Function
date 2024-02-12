""""
Q9.Define a function that accepts roll number and returns whether the student is present or absent. """

def check_attendance(roll_numb):
    presentstudents = [1,2,4,5,7,8,9,10]

    if roll_numb in presentstudents:
        return "Student is present."
    else:
        return "Student is absent."

roll_num = int(input("Enter the roll number to check whether the student is present or absent: "))
result = check_attendance(roll_num)
print(result)
