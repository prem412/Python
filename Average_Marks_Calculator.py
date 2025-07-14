#Mini Project: Average Marks Calculator

marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)
print(f"The average marks are: {average:.2f}")

# line3: Initializes an empty list to store marks.
# line4: Loops 5 times to get marks for each subject.
# line5: Prompts the user to input marks for each subject and appends them to the list.
# line6: appends the mark to the list.
# line7: 
# line8: Calculates the average of the marks.
# line9: Prints the average marks formatted to two decimal places