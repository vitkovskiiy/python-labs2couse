import os,json 


dirStudent = input("Choose the current name of students that you want to see: ")

if not os.path.exists('students.json'): 
    print("File don't exist")
else:
    with open('students.json','r', encoding = 'utf-8') as studentsFile:
        students = json.load(studentsFile);
        for student in students:
         if(student['name'] == dirStudent):
          print(f"{student['name']}, вік: {student['age']}, факультет:{student['faculty']}")
         
