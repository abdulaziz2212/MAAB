import csv 
from collections import defaultdict

header = ['Name','Subject','Grade']
data = [
    ['Alice', 'Math', 85],
    ['Bob', 'Science', 78],
    ['Carol', 'Math', 92],
    ['Dave', 'History', 74]
]

with open('grades.csv', mode='w',newline='') as file:
    writer = csv.writer(file)   
    writer.writerow(header)
    writer.writerows(data)


def csv_reader(csv_file):
    with open(csv_file, 'r') as file:
        reader=csv.DictReader(file, delimiter=',')
        all_rows=list(reader)
        print(all_rows)
        print()
        subject_grades=defaultdict(list)
        for row in all_rows:
            grade = int(row['Grade'])
            subject = row['Subject']
            subject_grades[subject].append(grade)
        
    with open('average_grades.csv', mode = 'w', newline='') as file:
        writer= csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])

        for subject,grades in subject_grades.items():
            average = sum(grades) / len(grades)
            writer.writerow([subject, round(average, 1)])

        print("Average grades have been written to 'average_grades.csv'")
    

csv_reader('grades.csv')

with open('average_grades.csv') as file:
    reader=csv.reader(file,delimiter=',')
    for row in reader:
        print(row)