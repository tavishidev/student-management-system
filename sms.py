'''STUDENT MANAGEMENT SYSTEM USING OOPS'''

class Student:
     def __init__(self,Student_id,name,age,marks):
        self.Student_id=Student_id
        self.name=name
        self.age=age
        self.marks=marks

     def display(self):
        print("\nStudent_id=",self.Student_id)
        print("name=",self.name)
        print("age=",self.age)
        print("marks=",self.marks)
       
class Studentmanagementsystem:
     def __init__(self):
         self.students=[]

     def add_student(self):
          Student_id=int(input("enter Student Id:"))
          for stud in self.students:
               if stud.Student_id==Student_id:
                    print("Data already exit")
                    return
          
          name=input("enter name:")
          age=int(input("enter age:"))
          marks=float(input("enter marks:"))

          s1=Student(Student_id,name,age,marks)
          self.students.append(s1)
          print("student added successfully")
 
 #view All students

     def view_student(self):
          if len(self.students)==0:
               print("no record found")
          else:
               print("\n-----student details----")
               for i in self.students:
                    i.display()
                   

#search for student using ID
     def search(self):
           student_id=int(input("enter Student Id to search:"))
           for id in self.students:
               if id.Student_id==student_id:
                   print("Student found!")
                   id.display()
                   return
               
#update a student marks
     def update_marks(self):
          student_id=int(input("enter Student Id to update:"))
         
          for student in self.students:
               if student.Student_id==student_id:
                   new_marks=float((input("enter new marks:"))) 
                   student.marks=new_marks
                   print("\n Marks updated successfully!")
                   return
               
          print("student not found")

#delete a student records
     def delete_record(self):
          student_id=int(input("enter Student Id to delete:"))

          for student in self.students:
               if student.Student_id==student_id:
                   self.students.remove(student)
                   print(f"Data of student with id {student_id} has been removed successfully")
                   return
          print("student not found!")

#display topper
     def display_topper(self):
         if len(self.students)==0:
             print("No Students Available!")
         else:
           topper=self.students[0]

           for stud in self.students:
             if stud.marks > topper.marks:
                 topper=stud
           print("\n-----Detail of topper-----")
           topper.display()


## main program
sms=Studentmanagementsystem()

while True:
    
     print("\n****** STUDENT MANAGEMENT SYSTEM ******")
     print("1.Add Student")
     print("2.View Students")
     print("3.Search Student")
     print("4.Update marks")
     print("5.Delete record")
     print("6.Display Topper")
     print("7.Exit")

     try:
          choice=int(input("ENTER YOUR CHOICE:"))
     except ValueError:
         print("please enter a valid number")
         continue

     if choice==1:
         sms.add_student()
     elif choice==2:
          sms.view_student()
     elif choice==3:
         sms.search()
     elif choice==4:
         sms.update_marks()
     elif choice==5:
         sms.delete_record()
     elif choice==6:
         sms.display_topper()
     elif choice==7:
         print("exist!!!!!!!!!!!!!!!!!!!")
         break
     else:
         print("invalid choice!")     
         

    



          
              
         


         
         
                   




          
         
         


        