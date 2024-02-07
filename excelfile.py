import csv
with open("student.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN","Movie", "protagonist"])
    writer.writerow([1,"Lord of the Rings","Frodo Baggins"])
    writer.writerow([2,"Harry Potter","Harry Potter"])